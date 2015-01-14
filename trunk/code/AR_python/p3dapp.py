#!/usr/bin/python

from direct.gui.OnscreenImage import OnscreenImage;
 
from direct.showbase.ShowBase import ShowBase;

import cv2;

from panda3d.core import Texture, CollisionRay,\
    CollisionHandlerQueue, CollisionTraverser,\
    CollisionNode, GeomNode, Shader, LMatrix4f, LPoint3f

from cvapp import cvApp;

class p3dApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self);
        
        # setup the environment or model
        self.model = \
            self.loader.loadModel("/usr/share/panda3d/models/box");
        self.model.reparentTo(self.render);
        self.model.setTag('Model', '1');
        self.model.setScale(1.5, 1.5, 1.5);
        
        # setup camera
        self.camera.setPos(5,5,5)
        self.camera.lookAt(0,0,0)
        
        # Disable mouse control
        self.disableMouse();
        
        # Handle mouse events.
        self.accept('mouse1', self.mouse_down);
        
        # convert image from opencv to panda3d texture
#         self.taskMgr.add(self.read_image_cv, "cvImageTask");
        
        # Setup collision handler
        self.handler = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('ColTraverser')
        self.traverser.traverse(self.model)
        self.ray = CollisionRay()
        pickerNode = CollisionNode('MouseRay')
        pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        pickerNP = self.camera.attachNewNode(pickerNode)
        pickerNode.addSolid(self.ray)
        self.traverser.addCollider(pickerNP, self.handler)
        
        self.load_shader();
        
        self.first_frame_loaded = False;

    def read_image_cv(self):
        """
        Pulls the next frame from the opencv part, and converts to a panda3d
        texture and display it on the screen.
        """
        cvim = self.cvapp.pull_frame()
        w = cvim.shape[1];
        h = cvim.shape[0];
        
        cvim = cv2.flip(cvim, 0);
        self.im = Texture("cvIm");
        self.im.setCompression(Texture.CMOff);
        self.im.setup2dTexture(w, h, Texture.TUnsignedByte, Texture.FLuminance);
        self.im.setRamImage(cvim);
         
        self.screen_im = OnscreenImage(parent=self.render2d, image=self.im, scale=(1, 1, 1), pos=(0, 0, 0));
        self.cam2d.node().getDisplayRegion(0).setSort(-20);
    
    def load_shader(self):
        """
        The function loads the vertex and fragment shader.
        It provides an example of sending the model-view-projection matrix
        to the shader program when it's calculated.
        """
        self.shader = Shader.load(Shader.SL_GLSL, "vertex.glsl", "fragment.glsl");
        self.model.set_shader(self.shader)
        self.model.set_shader_input("my_ModelViewProjectionMatrix", LMatrix4f())

    def mouse_down(self):
        """
        This function is called as a result of a mouse click.
        It gets the vertex that was clicked by the mouse.
        It sends the mouse position and the vertex position to the cv app.
        """
        if (self.first_frame_loaded == False):
            self.first_frame_loaded = True
            self.read_image_cv()
            return;
        
        xPos = self.mouseWatcherNode.getMouseX()
        yPos = self.mouseWatcherNode.getMouseY()
        self.ray.setFromLens(self.camNode, xPos, yPos)
        self.traverser.traverse(self.model)
        self.handler.sortEntries()
        if (self.handler.getNumEntries() > 0):
            entry = self.handler.getEntry(0) # CollisionEntry
            vpos = entry.getSurfacePoint(self.model)
            res = self.cvapp.mouse_clicked(LPoint3f(xPos, yPos), vpos)
            if (res == 1):
                self.read_image_cv()
        
    def set_cv_app(self, cvapp):
        self.cvapp = cvapp;
    

app3d = p3dApp()
appcv = cvApp(app3d)
app3d.set_cv_app(appcv)
app3d.run()

# TODO
# Create a class which reads the image,
#  A task is running in this object to retrieve the image
#   if it changes [For now single images]
#  An event is fired from here with the object and screen
#   coordinates, and received by the class.
#  Then the class displays another image, and does the same
#  
#  Once the 2 screen / object position pairs are gathered,
#   the calculation is done to retrieve the epipolar lines.
#  The lines will be drawn on the opencv image, and sent here
#   to be rendered.


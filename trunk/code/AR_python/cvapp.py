
#from p3dapp import p3dApp;
import numpy as np;
import cv2;
from panda3d.core import LPoint3f

class cvApp:
    
    def __init__(self, renderer):
        self.renderer = renderer;
        self.num_points = 0;
        self.mouse_vert_mat = cv2.cv.CreateMat(8, 3, cv2.CV_32F);
        
        self.image_idx = 1;
    
    def mouse_clicked(self, mouse_pos, vertex_pos):
        """
        Called by the 3D app when a mouse is clicked
        It is given a LPoint2f mouse position and the corresponding LPoint3f vertex
        position.
        It should store 4 of those, then tell the 3d app it's ready for the next frame.
        """
        print("cvapp ", mouse_pos, vertex_pos);
        
        cv2.cv.mSet(self.mouse_vert_mat, self.num_points*2, 0, mouse_pos.getX());
        cv2.cv.mSet(self.mouse_vert_mat, self.num_points*2, 1, mouse_pos.getY());
        cv2.cv.mSet(self.mouse_vert_mat, self.num_points*2, 2, 0);
        
        cv2.cv.mSet(self.mouse_vert_mat, self.num_points*2 + 1, 0, vertex_pos.getX());
        cv2.cv.mSet(self.mouse_vert_mat, self.num_points*2 + 1, 1, vertex_pos.getY());
        cv2.cv.mSet(self.mouse_vert_mat, self.num_points*2 + 1, 2, vertex_pos.getZ());
        
        self.num_points += 1;
        if (self.num_points == 4):
            
            ## THIS IS WHERE WE START COMPUTING THE BASIS VECTORS, ETC...
            
            print(np.asarray(self.mouse_vert_mat));
            
            self.image_idx += 1;
            return 1;
        else:
            return 0;
    
    def pull_frame(self):
        """
        Pulls the next opencv frame and return it.
        This is where any image annotations are added to the image
        For example, illustrative lines, etc..
        """
        if (self.image_idx == 1):
            cvim = cv2.imread("../data/20141020_214650.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE);
        elif (self.image_idx == 2):
            cvim = cv2.imread("../data/20141020_214655.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE);
        else:
            # Read the video frames.
            cvim = cv2.imread("../data/20141020_214650.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE);
            
        return cvim;

# [[-0.40249997 -0.40249997  0.        ]
#  [ 0.96434355  0.02363873  1.        ]
#  [ 0.00999999  0.00999999  0.        ]
#  [ 0.04425979  0.07017994  1.        ]
#  [ 0.37750006  0.37750006  0.        ]
#  [ 0.07205772  0.95052409  1.        ]
#  [ 0.00999999  0.00999999  0.        ]
#  [ 0.97701192  1.          0.14240193]]
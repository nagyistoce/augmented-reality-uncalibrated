 
from panda3d.core import LVector3f, LMatrix4f

def lookAt(pos, at):
    """
    Takes 2 LVector3f vectors,
    Returns the lookAt matrix Mat3d
    """
    
    # forward
    yaxis = at - pos
    print("forward ", yaxis)
    yaxis.normalize()
    
    # right
    xaxis = LVector3f.up().cross(yaxis)
    xaxis.normalize()
    print("right ", xaxis)
    
    # up
    zaxis = xaxis.cross(yaxis)
    zaxis.normalize()
    print("up ", zaxis)
    
    rmat = LMatrix4f()
    rmat.setRow(0, xaxis)
    rmat.setRow(1, zaxis)
    rmat.setRow(2, yaxis)
    
    tmat = LMatrix4f.translateMat(pos)
    
    print(rmat*tmat)
    
    return rmat * tmat

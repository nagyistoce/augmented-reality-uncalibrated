# First we have two views for an image
# And we select at least 4 points which are not coplanar in two views (they might look like the real basis )
# We considered that the 4 points is the basis of the affine space
#

//////////////////////////////////////////////////////////////

#from numpy import matrix
#from numpy import linalg
#A = matrix( [[1,2,3],[11,12,13],[21,22,23]]) # Creates a matrix.
#x = matrix( [[1],[2],[3]] )                  # Creates a matrix (like a column vector).
#y = matrix( [[1,2,3]] )
#print A.T                                    # Transpose of A.
#print A*x                                    # Matrix multiplication of A and x.
#print A.I                                    # Inverse of A.
#print linalg.solve(A, x)     # Solve the linear equation system.

/////////////////////////////////////////////////////////////////////

# [x,y,z,w]T is apoint on the vitrual object , [u,v,h]T is its projection 
# P3x4  is the matrix modeling the objest's projection onto the image plane,
# and C4x4 and O4x4 are the matrices coresponding to the object to world and the world to camera respectivily
# [u,v,h] = P3x4 C4x4 O4x4 [x',y',z',w']

# [x',y',z',w']T are the transformed coordinates of point [x,y,z,w]T 
# and L3x4 models the combined effecs of the change in the object's representation (the affine coordinates in our example)  
# [u,v,h] = L3x4 [x',y',z',w']


# Get a point in the affine coordinates
# after consider one of the 4 points is the origin and the other 3 is making the basis vectors
# L2x3 is the projection martix which form from three vector defining the 3D coordinate frameattached to the camera 
# L2x3 = [[(ub1-up0),(vb1-vp0)],[(ub2-up0),(vb2-vp0)],[(ub3-up0),(vb3-vp0)]] 
#[up,vp] = [[(ub1-up0),(vb1-vp0)],[(ub2-up0),(vb2-vp0)],[(ub3-up0),(vb3-vp0)]] x [x,y,z,] +,[up0,vp0]


# we have a superscribe m for all component remanis for the view of the image
# [up,vp,1] is the projection of the point p , b1,b2,and b3 are the basis points,
#[up0,vp0,1] is the projection of the origin and [x,y,z,1] is the homogenous vector of p'affine coordinates
# L3x4 = [[(ub1-up0),(vb1-vp0),0],[(ub2-up0),(vb2-vp0),0],[(ub3-up0),(vb3-vp0),0],[up0,vp0,1]]
  
#[up,vp,1] = [[(ub1-up0),(vb1-vp0),0],[(ub2-up0),(vb2-vp0),0],[(ub3-up0),(vb3-vp0),0],[up0,vp0,1]] x [x,y,z,1]

# When we have the projections of the pionts along two views we also can compute the affine coordinates
#[up,vp,1] = [[(u1b1-u1p0),(v1b1-v1p0),(u2b1-u2p0),(v2b1-v2p0)],[(u1b2-up0),(v1b2-vp0),(u2b2-u2p0),(v2b2-v2p0)],[(u1b3-u1p0),(v1b3-v1p0),(u2b3-u2p0),(v2b3-v2p0)],[u1p0,v1p0,u2p0,v2p0]] x [x,y,z,1]

# From the matrix L2x3 :1- we can form X (the direction of the rows of the camera expressed in the coordinate fram of the affine basis pionts)from the first row of the matrix
#2-  we can form Y (the direction of the columns of the camera expressed in the coordinate fram of the affine basis pionts)from the second row of the matrix


# The affine viewing direction W = X x Y
# guarantees that the set of points {p+tW , t from  R} that define the line of sight of a point p will project to a single pixel under (4)

# To order points along this direction we assign to each point p on the model a z-value
# The z-value is equal to [WT 0]T .p (the dot product) 


# u and v are the image coordinates of the p'projection and wis p'assigned z-value
# The 4x4 matrix is an affine generalization of the transformation matrix
# [u,v,w,1] = [[(ub1-up0),(ub2-up0),(ub3-up0),up0],[(vb1-vp0),(vb2-vp0),(vb3-vp0),vp0],[WT,z0],[0,0,0,1]] x [x,y,z,1]


# Epipolar line 
# first we have a point p its projection in the fisrt image is qL and in the second image is qR
# Then we have LL , LR are the upper 2x3 blocks of the affine view transformatio matrices associated with the first and second image 
# WL, WR are the corresponding viewing directions 
# the epipolar line of qL defined by a set { LR [ (LL)-1 qL + t WL ]t from R}







"""
1- select four or more corresponding fiducial points in the stereo pair and choose the affine basis
2- compute the matrices LL , LR , WL , WR with the left and the right camera
3- select four noncoplanar vertices on the 3D model of the virtual object 
4- specify the projections of them in the left image 
5- compute the epipolar lines of them in the right image 
6- 
7- specify the projection of them in the right image 
8- compute the affine space for them (points on the 3D model)
9- use (7) to compute the affine coordinates of all points o the virtual object from the affine coordinates of the points we select 

"""

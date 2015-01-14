clear all;
clc;
% read the images 
% select four points in the first imags  
% compute the matrices and the viewing direction 
% select noncoplanar vetrices on the 3D model 
% specify the projections of the points 
% compute the epipolar line s corresponding to the points
% specify point collinearity and coplanarity constraints for one or more 

im1 = imread('../data/20141020_214650.jpg');
%im2 = imread('../data/20141020_214655.jpg');

colormap gray
imagesc(im1);
%imagesc(im2);

points1 = [ 309 , 704 ;
            1137 , 503 ;
            998 , 2331 ;
            1798 , 1899 ]'
         
points2 = [ 623 , 836 ;
            1283 , 876 ; 
            452 , 2137 ; 
            1198 , 2396 ]'



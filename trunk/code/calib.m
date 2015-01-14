clear all; clc; close all;

% Left / RIght images.
imL = imread('../data/20141020_214650.jpg');
imR = imread('../data/20141020_214655.jpg');

% 4 Corresponding points.
pL = [309 704;
      1137 503;
      998 2331;
      1798 1899];

pR = [623 836;
      1283 876;
      452 2137;
      1198 2396];
  
% objf = read_wobj('../data/models/example1.obj');
% plot3(objf.veritces(:,1), objf.veritces(:,2), objf.veritces(:,3));

% Create the affine bases for left and right.
% b1 = p2 - p1; b2 = p3 - p1; b3 = p4 - p1;
bL = pL(2:4,:)-repmat(pL(1,:),3,1);
bR = pR(2:4,:)-repmat(pR(1,:),3,1);

figure;
colormap gray;
subplot(1,2,1);
imagesc(imL);
% axis off;
% axis equal;
hold on;
plot(pL(:,1), pL(:,2), 'o');

%% Compute camera matrix in left / right.
% Compute the Camera matrices cR / cL, and view direction vR, vL in affine
% coordinates (4)
% c = [ub1, ub2, ub3; vb1, vb2, vb3]
% v = [ub1, ub2, ub3] x [vb1, vb2, vb3]'
camL = bL';
vL = cross(camL(1,:), camL(2,:)');
camR = bR';
vR = cross(camR(1,:), camR(2,:)');

%% Model vertices and their projections.
% Select 4 vertices from the model,
% and define their projections on the image plane on the right.
% Assume a cube, and we've select 4 non co-planar vertices.
% THIS REPLACES THE USER SELECTION STAGE
mod = [0 0 1;
       1 0 1;
       0 1 0;
       1 1 0];
modProjL = [944  1737;
            1197 1606;
            1077 1056;
            1227 1036];

% plot model vertex projections.
for i = 1:4
    plot(modProjL(i,1), modProjL(i,2), 'x', 'Color', [abs(cos(i)) 0.7 abs(sin(i))]);
end

%% Compute epipolar lines
% compute the epipolar lines  from the projections
camLinv = pinv(camL);

t1 = 0.0000001;
ep1 = (camR * ((camLinv * modProjL') + repmat(t1 * vL', 1, 4)))';

t2 = 0.0000001;
ep2 = (camR * ((camLinv * modProjL') + repmat(t2 * vL', 1, 4)))';

maxX = size(imR,1);

% plot results
subplot(1,2,2);
imagesc(imR);
% axis off;
% axis equal;
hold on;
plot(pR(:,1), pR(:,2), 'o');
for i = 1:4
    p = [ep1(i,1) ep1(i,2);
         ep2(i,1) ep2(i,2)];
    m = (p(1,1)-p(2,1)) / (p(2,1)-p(2,2));
    b = p(1,2) - (m * p(1,1));
    
    px  = [0 b;
           maxX (maxX*m+b)];
    plot(px(:,1), px(:,2), 'x-', 'Color', [abs(cos(i)) 0.7 abs(sin(i))]);
end

%% Select point projections in the right image.
%
% REPLACES THE USER SELECTION PART

%% Basis affine coordinates
% We can find the affine coordinates of the basis points.
% Using the viewing direction and basis vectors, a 3D point's project
% can be found using the following equation.
% [u v w 1]' = [ub1, ub2, ub3, up0;
%               vb1, vb2, vb3, vp0;
%               v1,  v2,  v3,  z0;
%               0,   0,   0,   1;] * [x;
%                                     y;
%                                     z;
%                                     1];
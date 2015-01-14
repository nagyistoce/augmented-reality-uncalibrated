
clear all; clc; close all;

myaxes = axes('xlim', [-3 3] ,'ylim' , [-3 3] ,'zlim', [-3 3]);
view(3);
axis equal;
axis off;

objf = read_wobj('./data/models/example5.obj');
c(size(objf.vertices,1):1) = 1;
%mesh(objf.vertices(:,1)', objf.vertices(:,2)', objf.vertices(:,3)');
h = patch('Faces', objf.objects.data.vertices, 'Vertices', objf.vertices,'FaceVertexCData', c);

% while (true)
%    camorbit(30*0.02, 0);
%    waitfor(0.02);
%    drawnow;
% end

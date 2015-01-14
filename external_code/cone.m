%% set axis and figure 

myaxes = axes('xlim', [-2 2] ,'ylim' , [-2 10] ,'zlim', [-1.5 1.5]);
view(3);
grid on;
axis equal;
hold on
xlabel('x')
ylabel('y')
zlabel('z')

%% generate the clyinder , the cone and the sphere

[ xcylinder ycylinder zcylinder ] = cylinder([.2 .2]);
[ xcone ycone zcone ] = cylinder([0.1 0.0]); %cone
[ xsphere ysphere zsphere ] = sphere();

%% plot different orientations of these shapes 
% assign all surfaces to a variable h
h(1) = surface(xcylinder , ycylinder , zcylinder);
h(2) = surface(zcylinder , xcylinder , ycylinder);
h(3) = surface(-zcylinder , xcylinder , ycylinder);

h(4) = surface(-zcylinder , xcylinder , ycylinder+1);
h(5) = surface(zcylinder , xcylinder , ycylinder+1);
h(6) = surface(zcylinder , 0.5*xcylinder , ycylinder+0.5);
h(7) = surface(-zcone , 0.5*xcone , ycylinder+0.5);
h(8) = surface(0.25*xsphere+1 , 0.25*ysphere , 0.25*zsphere);
h(9) = surface(0.25*xsphere-1 , 0.25*ysphere , 0.25*zsphere);
h(10) = surface(0.25*xsphere+1 , 0.25*ysphere , 0.25*zsphere+1);
h(11) = surface(0.25*xsphere-1 , 0.25*ysphere , 0.25*zsphere+1);


%% create a group object and parent surfaces 

combinedobject = hgtransform('parent',myaxes);
set(h,'parent',combinedobject)
drawnow

%% define camera movement
% 
% while (true)
%     camorbit(360*0.02, 0);
%     pause(0.02);
% end

%% define the motion coordinates


longitude = 0:10;  % x-direction traslation 
latitude = [0 1 1 1 0 0 -1 -1 -1 -1];  % y-direction translation
altitude = [0 1 1 1 0 0 -1 -1 -1 -1];  % z-direction translation

bearing = [0 10 20 30 20 10 0 -10 -20 -30];



%% animate by using the function makehgtform

for i = 1:length(latitude)
    
    translation = makehgtform('translate' , [latitude(i) longitude(i) altitude(i)]);
    %set(combinedobject , 'matrix' , translation);

%     rotation1 = makehgtform('xrotate', pi/180*(bearing(i)))
%      set(combinedobject , 'matrix' , rotation1);
%
      rotation2 = makehgtform('xrotate', pi/180*(bearing(i)))
      set(combinedobject , 'matrix' , rotation2);
%
%      rotation3 = makehgtform('xrotate', pi/180*(bearing(i)))
%      set(combinedobject , 'matrix' , rotation3);
%
%      scaling = makehgtform('scale' , 1-(i/20));
%      set(combinedobject, 'matrix' ,scaling);


%      % the individual transformation can be combined
%      set(combinedobject , 'matrix'
%      ,translation*rotation1*rotation2*rotation3*scaling);

    pause(0.3)
    
end


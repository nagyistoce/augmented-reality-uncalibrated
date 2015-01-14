
uniform mat4 p3d_ModelViewProjectionMatrix;
in vec4 p3d_Vertex;
in vec4 p3d_Color;

uniform mat4 my_ModelViewProjectionMatrix;

varying vec4 col;

void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
  col = p3d_Color;
}

varying vec4 col;

void main() {
  gl_FragColor = vec4(col.r, col.g, col.b, col.a);
}
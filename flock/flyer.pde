class flyer {
  PVector dir;
  PVector pos;
  float vel;
  
  flyer() {
    pos = new PVector(width/2, height/2);
    dir = new PVector(1, 0);
    vel = 0.8;
  }
  
  void draw() {
    PVector nDir = this.dir.copy();
    nDir.normalize();
    triangle(pos.x + (nDir.x * 15), pos.y + (nDir.y * 15),
             pos.x + (nDir.y * -5), pos.y + (nDir.x * 5),
             pos.x + (nDir.y * 5), pos.y + (nDir.x * -5));
  }
  
  void move() {
    pos.add(PVector.mult(dir, vel));
    pos.x = (pos.x + width) % width;
    pos.y = (pos.y + height) % height;
    dir.normalize();
  }
}
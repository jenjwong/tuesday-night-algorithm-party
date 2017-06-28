flyer fly;
flyer[] flock;
int nFlock;
float perceptionRadius = 80;


void setup() {
  fullScreen(2);
  frameRate(60);
  
  nFlock = 400;
  fly = new flyer();
  flock = new flyer[nFlock];
  
  for (int i = 0; i < nFlock; ++i) {
    flock[i] = new flyer();
    flock[i].dir = PVector.random2D();
    flock[i].pos.x = random(width);
    flock[i].pos.y = random(height);
  }
}


void draw() {
  noFill();
  background(255);
  
  strokeWeight(1);
  stroke(160);
  for (flyer f : flock) {
    f.move();
    f.draw();
    line(f.pos.x, f.pos.y, f.pos.x + (f.dir.x * 20), f.pos.y + (f.dir.y * 20));
  }

  strokeWeight(2);
  stroke(0);
  fly.move();
  fly.draw();
  
  strokeWeight(1);
  stroke(220, 140, 140);
  ellipse(fly.pos.x, fly.pos.y, perceptionRadius*2, perceptionRadius*2);
  for (flyer f : near(fly)) {
    f.draw();
    line(f.pos.x, f.pos.y, f.pos.x + (f.dir.x * 20), f.pos.y + (f.dir.y * 20));
  }
  
  if (frameCount % 1 == 0) {
    for (flyer f : flock) {
      reorientFlyer(f);
    }
  }
  
  //for (flyer f : flock) {
  //  f.dir.rotate(f.turn);
  //}
}


void keyPressed() {
  if (key == 'q' || key == 'Q') {
    exit();
  } else if (keyCode == LEFT) {
    fly.dir.rotate(-.04);
  } else if (keyCode == RIGHT) {
    fly.dir.rotate(.04);
  } else if (key == 'r') {
    perceptionRadius--;
  } else if (key == 'R')  {
    perceptionRadius++;
  }
}


ArrayList<flyer> near(flyer o) {
  ArrayList<flyer> res = new ArrayList<flyer>();
  
  for (flyer f : flock) {
    if (o != f && o.pos.dist(f.pos) <= perceptionRadius) {
      res.add(f);
    }
  }
  
  return res;
}


void reorientFlyer(flyer f) {
  ArrayList<flyer> neighbors = near(f);
  
  if (neighbors.size() == 0) {
    f.turn = 0;
    return;
  }

  float avgAngle = atan2(f.dir.y, f.dir.x);
  for (flyer n : neighbors) {
    avgAngle += atan2(n.dir.y, n.dir.x);
  }
  avgAngle = avgAngle / (neighbors.size() + 1);
  
  float fAngle = atan2(f.dir.y, f.dir.x);
  fAngle = fAngle + ((avgAngle - fAngle) / 10);
  
  PVector avgDir = PVector.fromAngle(fAngle);
  f.dir = avgDir;
  //float diff = PVector.angleBetween(f.dir, avgDir);
  //if (fAngle > avgAngle) {
  //  f.turn = max(-0.5, -diff/10);
  //} else {
  //  f.turn = min(0.5, diff/10);
  //}
}
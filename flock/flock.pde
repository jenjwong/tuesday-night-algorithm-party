import java.util.Collections;
import java.util.Comparator;


boolean showDebug;

flyer fly;
flyer[] flock;
int nFlock;
float perceptionRadius = 80;
float idealSeparation = 30;


void setup() {
  fullScreen(2);
  frameRate(60);
  
  showDebug = false;
  
  nFlock = 1000;
  fly = new flyer();
  flock = new flyer[nFlock];

  for (int i = 0; i < nFlock; ++i) {
    flock[i] = new flyer();
    flock[i].dir = PVector.random2D();
    //flock[i].dir = PVector.fromAngle(random(3*PI/4, 5*PI/4));
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
    if (showDebug) {
      line(f.pos.x, f.pos.y, f.pos.x + (f.dir.x * 20), f.pos.y + (f.dir.y * 20));
    }
  }

  strokeWeight(2);
  stroke(0);
  fly.move();
  fly.draw();

  if (showDebug) {
    strokeWeight(1);
    stroke(220, 140, 140);
    ellipse(fly.pos.x, fly.pos.y, perceptionRadius*2, perceptionRadius*2);
    for (flyer f : near(fly)) {
      f.draw();
      line(f.pos.x, f.pos.y, f.pos.x + (f.dir.x * 20), f.pos.y + (f.dir.y * 20));
    }
  }

  for (flyer f : flock) {
    reorientFlyer(f);           // make them flock
    repelAndAttractFlyer(f);    // force directed formation, prevent bunching
  }
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
  } else if (key == 'd') {
    showDebug = !showDebug;
  }
}


ArrayList<flyer> near(flyer o) {
  return near(o, perceptionRadius);
}


ArrayList<flyer> near(flyer o, float radius) {
  ArrayList<flyer> res = new ArrayList<flyer>();
  
  for (flyer f : flock) {
    if (o != f && o.pos.dist(f.pos) <= radius) {
      res.add(f);
    }
  }
  
  return res;
}


void reorientFlyer(flyer f) {
  // The purpose of this method is to make a flyer change direction slightly based on other flyers nearby.
  // It will try to match their general direction.
  ArrayList<flyer> neighbors = near(f);

  // Compute in newDir the centroid of f and all its neighbors.
  // (No need to scale it yet, we just need the direction of the centroid relative to 0.)
  PVector newDir = f.dir.copy();
  for (flyer n : neighbors) {
    newDir.add(n.dir);
  }
  
  // Handle the rare case where the centroid is the origin.
  if (newDir.mag() <= 0.00001) {
    while (newDir.mag() <= 0.00001) {
      // miraculously, centroid is centered on f, to prevent the flyer from stopping completely, choose a random new direction
      newDir = PVector.random2D();
    }
  } else {
    // Normalize newDir just to be consistent with how we handle directions in general.
    newDir.normalize();
  }

  // Compute the difference from f's angle and the centroid's angle.  Adjust it so it's a number between -PI and PI.
  // We need to do this because we are NOT going to set f.dir to be newDir directly, instead we want f to slowly turn
  // towards newDir, and if we don't normalize the angles in this way, then all flyers tend to go towards 0: all fly
  // to the right.
  float diff = atan2(newDir.y, newDir.x) - atan2(f.dir.y, f.dir.x);
  if (diff > PI) {
    diff = diff - 2*PI;
  } else if (diff <= -PI) {
    diff = diff + 2*PI;
  } // else abs(diff) <= PI, we're good.
  
  // Rotate f so it heads towards newDir.
  f.dir.rotate(diff / 10); // Smoothing constant

  if (showDebug) {
    strokeWeight(1);
    stroke(0, 255, 0);
    line(f.pos.x, f.pos.y, f.pos.x + newDir.x * 30, f.pos.y + newDir.y * 30);
  }
}


void repelAndAttractFlyer(final flyer f) {
  ArrayList<flyer> neighbors = near(f);
  PVector offsetDir;
  PVector forceAdjustment = new PVector();
  float offsetDist;

  Comparator comp = new Comparator<flyer>() {
    public int compare(flyer f1, flyer f2) {
      float diff = PVector.dist(f2.pos, f.pos) - PVector.dist(f1.pos, f.pos);
      if (diff > 0) {
        return -1;
      } else if (diff < 0) {
        return 1;
      } else {
        return 0;
      }
    }
  };
  
  // Favor closest neighbors.
  Collections.sort(neighbors, comp);

  int count = 0;
  for (flyer n : neighbors) {
    if (++count > 4) {  // Limit the number of neighbors that affect f's formation.
      break;
    }

    offsetDir = PVector.sub(f.pos, n.pos);
    offsetDist = offsetDir.mag();
    offsetDir = offsetDir.normalize().mult(idealSeparation - offsetDist);
    forceAdjustment.add(offsetDir);
  }

  forceAdjustment.mult(1 / 1000.0); // Smoothing constant
  f.dir.add(forceAdjustment);
}
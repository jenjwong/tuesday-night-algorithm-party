// Stack Max: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and max should all operate in 0(1) time.
// Hints: #27, #59, #78

// constant time and linear space? (each value pushed into the outer array is stored as a tupple)

// Input: numbers
// Output: numbers last in first out and min
// constraints: constant time
// edgecases: duplicate max, no more items in stack

// First solution stores two element arrays made up of value and current max.

class Stack {
  constructor() {
    this.storage = {};
    this.count = 0;
    this.max = -Infinity;
  }

  push(val) {
    this.max = Math.max(this.max, val);
    this.storage[this.count] = [val, this.max];
    this.count += 1;
  }

  pop() {
    this.count -= 1;
    if (this.count >= 0) {
      const popped = this.storage[this.count];
      this.max = popped[1];
      delete this.storage[this.count];
      return popped;
    }
    return null;
  }

  min() {
    return this.storage[this.count - 1][1];
  }
}

const stacked = new Stack();
stacked.push(1);
stacked.push(7);
stacked.push(100);
stacked.push(8);
console.log(stacked.storage, 'storage');
console.log(stacked.max(), 'max');
console.log(stacked.pop(), 'popped');
console.log(stacked.pop(), 'popped');
console.log(stacked.storage, 'storage');
console.log(stacked.max(), 'max');


// constant time, but more efficient space than solution above
// ** what is the space complexity?
  // The first solution stores tuples instead of single intergers in a storage array
  // The second solution creates one new array and stores integers in it

class Stack {
  constructor() {
    this.count = 0;
    this.storage = {};
    this.maxHistory = [-Infinity];
  }

  push(val) {
    this.count += 1;
    if (val >= this.maxHistory[this.maxHistory.length - 1]) {
      this.maxHistory.push(val);
    }
    this.storage[this.count] = val;
  }

  pop() {
    if (this.count >= 1) {
      const popped = this.storage[this.count];
      if (popped === this.maxHistory[this.maxHistory.length - 1]) {
        this.maxHistory.pop();
      }
      delete this.storage[this.count];
      this.count -= 1;
      return popped;
    }
    return null;
  }

  max() {
    return this.maxHistory[this.maxHistory.length - 1];
  }
}

const stacked = new Stack();
stacked.push(1);
stacked.push(7);
stacked.push(100);
stacked.push(8);
console.log(stacked.storage, 'storage');
console.log(stacked.max(), 'max 100');
console.log(stacked.pop(), 'popped 8');
console.log(stacked.pop(), 'popped 100');
console.log(stacked.storage, 'storage');
console.log(stacked.max(), 'max 7');

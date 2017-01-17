// Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack (that is, pop ( ) should return the same values as it would if there were just a single stack).
// FOLLOW UP
// ImplementafunctionpopAt(int index)whichperformsapopoperationonaspecificsub-stack. Hints: #64, #87

// Input: integers
// Output: data structure described above
// Contraints: none
// Edge-cases:
//   push: one stack is full and need to use next stack
//   pop: one stack is empty and need to use prev stack
//   creating first stack

// constant time and linear space

class PlateStack {
  constructor(limit) {
    this.limit = limit;
    this.storage = [];
    this.arrayCount = 0;
    this.count = 0;
  }

  push(val) {
    if (this.storage[this.arrayCount] === undefined || this.count >= this.limit) {
      this.arrayCount += 1;
      this.storage[this.arrayCount] = {};
      this.count = 1;
      this.storage[this.arrayCount][this.count] = val;
    } else {
      this.count += 1;
      this.storage[this.arrayCount][this.count] = val
    }
  }

// leaves an array full of empty objects; could use splice if this were a concern
  pop() {
    if (this.arrayCount >= 1) {
      if (this.count < 1 && this.arrayCount > 1) {
        this.count = this.limit;
        this.arrayCount -= 1;
      }
      let popped = this.storage[this.arrayCount][this.count];
      delete this.storage[this.arrayCount][this.count];
      this.count -= 1;
      return popped;
    }
    return -1;
  }
}

const plates = new PlateStack(3)
plates.push(111);
plates.push(222);
plates.push(333);
plates.push(444);
plates.push(555);
console.log(plates.storage)
console.log(plates.pop()) // 555
console.log(plates.pop())  // 444
console.log(plates.pop())  // 333
console.log(plates.storage) // {1: 111, 2: 222}
console.log(plates.pop()) // 222
console.log(plates.pop()) // 111
console.log(plates.pop()) // -1
console.log(plates.storage) // storage: []

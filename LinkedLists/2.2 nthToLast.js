// Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
// Hints: #8, #25, #47, #67, # 726

// Input: linked list
// Output: linked list minus duplicates
// Constraints: singly linked list
// Edge Cases: nth doesn't exisit

// linear time and constant space


// create count variable
// create node variable set to head
// create slowPointer variable set to null

// while there are nodes in list
  // increment count
  // if the count is equal to nth
    // set the slowPointer to the head
  // if the count is greater than nth
    // set slowPointer to slowPointer.next
  // set node to next node

// return slowPointer

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  addToHead(val) {
    const node = new Node(val);
    const oldHead = this.head;
    if (!this.head) {
      this.tail = node;
    }
    this.head = node;
    this.head.next = oldHead;
  }

  nthToLast(nth) {
    let count = 0;
    let node = this.head;
    let slowPointer = null;

    while (node) {
      count += 1;
      if (count === nth) {
        slowPointer = this.head;
      }
      if (count > nth) {
        slowPointer = slowPointer.next;
      }
      node = node.next;
    }
    return slowPointer;
  }
}

const print = (ll) => {
  let node = ll.head;
  while (node) {
    console.log(node.val);
    node = node.next;
  }
};

const ll = new LinkedList();
ll.addToHead(11);
ll.addToHead(22);
ll.addToHead(33);
ll.addToHead(44);
ll.addToHead(55);
ll.addToHead(66);
ll.addToHead(77);
ll.addToHead(88);

// prints linked list
console.log('linkedList')
print(ll);
console.log(ll.head)
console.log(ll.head.next)
console.log(ll.head.next.next)

console.log('5', ll.nthToLast(5))
console.log('8', ll.nthToLast(8))
console.log('null', ll.nthToLast(11))

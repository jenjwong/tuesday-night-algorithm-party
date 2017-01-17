// Remove Dups: Write code to remove duplicates from an unsorted li nked list. FOLLOW UP
// How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40

// Input: linked list
// Output: linked list minus duplicates
// Constraints: singly linked list
// Edge Cases: duplicates are at the end of list (next = null), triplicates ect

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

  // create valueSeen hashDictionary
  // set node to head
  // set node.val as property in valueSeen hashDictionary
    // traverse through LinkedList
      // if node.val of next node exisits in dictionary
        // save reference to currentNode
        // while there is a next.next node and value of next and next.next is the same
          // set node to node.next
        // set currentNode to node.next.next
      // node.next.val in valueSeen
      // set node to node.next
// (checking for duplicates one node ahead of currentnode allows for deletion in linear time)



  removeDuplicates() {
    const valueSeen = {};
    let node = this.head;
    if (this.head) {
      valueSeen[node.val] = true;
    }
    while (node) {
      if (node.next) {
        if (valueSeen[node.next.val]) {
          const currentNode = node;
          while (node.next.next && node.next.val === node.next.next.val) {
            node = node.next;
          }
          currentNode.next = node.next.next;
        }
        valueSeen[node.next.val] = true;
      }
      node = node.next;
    }
  }
}

const print = (ll) => {
  node = ll.head
  while (node) {
    console.log(node.val)
    node = node.next
  }
}

var ll = new LinkedList();
ll.addToHead(77);
ll.addToHead(99);
ll.addToHead(99);
ll.addToHead(99);
ll.addToHead(99);
ll.addToHead(88);
ll.addToHead(88);
ll.addToHead(66);

console.log('handles duplicates in middle of list')
// prints linked list
console.log('origional linkedList')
print(ll);

ll.removeDuplicates()
// prints linked list without dupes
console.log('removes duplicates')
print(ll);


console.log('handles duplicates at end of list')
var ll = new LinkedList();
ll.addToHead(99);
ll.addToHead(99);
ll.addToHead(99);
ll.addToHead(99);
ll.addToHead(88);
ll.addToHead(88);
ll.addToHead(66);

// prints linked list
console.log('origional linkedList')
print(ll);

ll.removeDuplicates()
// prints linked list without dupes
console.log('removes duplicates')
print(ll);


console.log('handles unique list')
var ll = new LinkedList();
ll.addToHead(99);
ll.addToHead(88);
ll.addToHead(66);

// prints linked list
console.log('origional linkedList')
print(ll);

ll.removeDuplicates()
// prints linked list without dupes
console.log('removes duplicates')
print(ll);

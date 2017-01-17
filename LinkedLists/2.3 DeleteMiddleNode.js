// Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
// EXAMPLE
// Input: the node c from the linked list a - >b- >c - >d - >e- >f
// Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f Hints: #72


// create a function that takes an nth
  // create a counter set to 0
  // create a var called node and set to head
  // while there are nodes in the list
    // if counter equals nth
      // set current node value to next node value
      // set current node next to next node next
      // (if doubly linked list set next node's prev value to current node)

// removeNth has O(n) time complexity and O(1) space complexity
// traversing the list is linnear and the actual deletion happens in constant time


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

        removeNth(nth) {
          let count = 0;
          let node = this.head;
          while (node) {
            count += 1;
            if (count === nth) {
              let deletedValue = node.val;
              node.val = node.next.val;
              node.next = node.next.next;
              return deletedValue;
            }
            node = node.next;
          }
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


      console.log('removed 5th node 44',   ll.removeNth(5))

      print(ll);

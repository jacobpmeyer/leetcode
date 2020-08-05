// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeKthNodeFromEnd(head, k) {
  let fast = head;
  let slow = head;
  let count = 1;
  while (count <= k) {
    fast = fast.next;
    count += 1;
  }
  if (fast === null) {
    head.value = head.next.value;
    head.next = head.next.next;
    return;
  }
  while (fast.next !== null) {
    fast = fast.next;
    slow = slow.next;
  }
  slow.next = slow.next.next;
}

// Do not edit the line below.
exports.LinkedList = LinkedList;
exports.removeKthNodeFromEnd = removeKthNodeFromEnd;

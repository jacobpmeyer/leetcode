// You are given two non-empty linked lists representing two non-negative integers.
// The digits are stored in reverse order and each of their nodes contain a single
// digit. Add the two numbers and return it as a linked list.

import { node } from "prop-types";

// You may assume the two numbers do not contain any leading zero, except the
// number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

var addTwoNumbers = function (l1, l2) {
  let leftNode = l1;
  let rightNode = l2;

  let left = "";
  let right = "";

  while (leftNode || rightNode) {
    if (leftNode) {
      left += leftNode.val.toString();
      leftNode = leftNode.next;
    }
    if (rightNode) {
      right += rightNode.val.toString();
      rightNode = rightNode.next;
    }
  }
  return stringAdder(left, right);
};

const stringAdder = (left, right) => {
  let num = parseInt(left[0]) + parseInt(right[0]);
  node = new ListNode(num % 10);
  const head = node;
  let remainder = Math.floor(num / 10);
  let strLength = left.length > right.length ? left.length : right.length;
  let i = 0;
  for (let i = 1; i < strLength; i++) {
    let leftNum = 0;
    let rightNum = 0;

    if (left[i]) leftNum = parseInt(left[i]);
    if (right[i]) rightNum = parseInt(right[i]);

    num = leftNum + rightNum + remainder;

    node.next = new ListNode(num % 10);
    node = node.next;
    remainder = Math.floor(num / 10);
  }
  if (remainder) node.next = new ListNode(remainder);
  return head;
};

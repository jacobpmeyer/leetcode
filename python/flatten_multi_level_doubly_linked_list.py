"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return 

        pHead = Node(0, None, head, None)
        self.flattenRecur(pHead, head)
        pHead.next.prev = None
        return pHead.next


    def flattenRecur(self, prev: "Node", curr: "Node") -> "Node":
        # Return the tail
        if curr is None:
            return prev

        prev.next = curr
        curr.prev = prev

        tempNext = curr.next

        tail = self.flattenRecur(curr, curr.child)
        # curr.child = None
        return self.flattenRecur(tail, tempNext)


class Solution(object):
    def flatten(self, head):
        if not head:
            return

        # Create a dummy head so that we never have to check for previous 
        # being None.
        pseudoHead = Node(0,None,head,None)

        # Set our previous variable to pseudoHead for the first pass of our loop
        prev = pseudoHead

        # Instantiate our stack, with the head as the first value.
        stack = [head]

        # Loop over our stack as long as it is valid
        while stack:
            # set pop the first thing off the stack and set it to current
            curr = stack.pop()

            # Establish relationship between the previous var and the curr var
            prev.next = curr
            curr.prev = prev

            # Push the current Node's next to the stack before the child node
            if curr.next:
                stack.append(curr.next)
 
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next
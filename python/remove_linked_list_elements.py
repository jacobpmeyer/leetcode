# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newFirst = ListNode(0)
        newFirst.next = head
        curr = newFirst
        while curr is not None:
            while curr.next is not None and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return newFirst.next
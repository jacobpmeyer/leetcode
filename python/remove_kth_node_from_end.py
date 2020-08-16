# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    count = 0
    fast = head
    slow = head
    while count < k:
        fast = fast.next
        count += 1
    if fast is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
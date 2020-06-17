# This is an input class. Do not edit.
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None


def removeKthNodeFromEnd(head, k):
	counter = 0
	first = head
	second = head
	while counter < k:
		counter += 1
		first = first.next
	if first is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while first.next is not None:
		first = first.next
		second = second.next
	second.next = second.next.next
	return head

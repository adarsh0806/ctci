# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes 1->2->3->5.

class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value):
		self.value = value
		self.next = None

class RemoveNthEnd(object):
	"""docstring for ClassName"""
	def remove_nth_from_end(self, head, n):
		dummy = ListNode(0)
		dummy.next = head
		
		# get length
		length = 0
		prev = dummy
		while prev.next:	
			length += 1
			prev = prev.next
		
		# find nth from end element and remove it
		prev = dummy
		count = 0
		while prev.next:
			current = prev.next
			if count == length - n:
				prev.next = current.next
				break
			else:
				count += 1
				prev = prev.next

		return dummy.next


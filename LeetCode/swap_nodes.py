"""
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		if self:
			return '{} -> {}'.format(self.val, self.next)

class SwapNodes(object):
	"""docstring for SwapNodes"""
	def swap_nodes(self, head):
		dummy = current= ListNode(0)
		dummy.next = head
		while current.next and current.next.next:
			n_one = current.next
			n_two = current.next.next
			n_three = current.next.next.next

			current.next = n_two
			n_two.next = n_one

			n_one.next = n_three
			current = n_one

		return dummy.next

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	print SwapNodes().swap_nodes(head)

"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + 
	   (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		self.next = None

class Addition(object):
			"""docstring for Addition"""
			def add_two_ll(self, l1, l2):
				dummy = Node(0)
				carry = 0
				current = dummy
				x1 = []
				
				while l1 or l2:
					value = 0

					if l1:
						value += l1.value
						l1 = l1.next
											
					if l2:
						value += l2.value
						l2 = l2.next
						x1.append(value)
					
					carry = value / 10
					value = value % 10
					print '	carry: ', carry
					print '	value: ', value

					current.next = Node(value)
					# print 'current.next.value: ',current.next.value
					current = current.next
					print 'current.value: ', current.value

				# if carry == 1:
				# 	current.next = Node(1)

				print x1
				return dummy.next

if __name__ == '__main__':
	l1 = Node(2)
	l1.next = Node(4)
	l1.next.next = Node(3)

	l2 = Node(5)
	l2.next = Node(6)
	l2.next.next = Node(4)
	
	result = Addition().add_two_ll(l1, l2)
	print "{0} -> {1} -> {2}".format(result.value, result.next.value, result.next.next.value)



						
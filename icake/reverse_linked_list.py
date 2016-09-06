# T: O(n), S: O(1)
def reverse_ll(l):
	current = l.head
	previous = None
	next_node = None
	while current:
		next_node = current.next_node
		# reverse direction
		current.next_node = previous
		# move forward
		previous = current
		current = next_node
	return previous
# Merge two sorted lists iteratively and recursively
def merge_two_ll(l1, l2):
	dummy = current = ListNode(0)
	while l1 and l2:
		if l1.val < l2.val:
			current = l1.next
			l1 = l1.next
		else:
			current = l2.next
			l2 = l2.next
		current = current.next
	if l1:
		current.next = l1
	else:
		current.next = l2
	return dummy.next

def merge_two_ll_recursive(l1,l2):
	if not l1 or l2:
		return l1 or l2
	if l1.val < l2.val:
		l1.next = merge_two_ll_recursive(l1.next,l2)
	else:
		l2.next = merge_two_ll_recursive(l1, l2.next)

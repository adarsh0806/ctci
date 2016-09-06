# T: O(n), S: O(1)
def check_cycle(self):
	p1 = self.head
	p2 = self.head
	while p1 != None and p1.next != None:
		p2 = p2.next
		p1 = p1.next.next
		# point of contact 
		if p1 == p2:
			return True
	return False
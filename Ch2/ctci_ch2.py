# Implementation of linked list from scratch
class Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	# returns the stored data 
	def get_data(self):
		return self.data

	# returns the next node (the node to which the object node points), 
	def get_next(self):
		return self.next_node

	# reset the pointer to a new node 
	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	def display(self):
		current = self.head
		while current != None:
			print current.data
			current = current.next_node

	# Insert: inserts a new node into the list
	def insert(self, data):
		# Insert at the start of the list
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	# Size: returns size of list
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count


	# Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error
	def search(self, data):
		found = False
		current = self.head
		while current and found is False:
			if current.get_data() == data:
				found = True
				return current
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")


	# Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error
	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else: 
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError('Data not in linked list.')
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

# Set up linked list
ll = LinkedList()
data= [1,2,3,4,5,6,6,4,3]  
for i in data:
	ll.insert(i)

# print ll.display()
# print ll.size()
# print ll.search(2)

# 2.1 Remove duplicates from an unsorted linked list
def remove_duplicates(self):
	dictionary = {}
	current = self.head
	previous = None
	while current:
		if current.get_data() in dictionary:
			previous.set_next(current.get_next())
			current = current.get_next()
		else:
			# Add element to dictionary
			dictionary[current.get_data()] = True
			previous = current
			current = current.get_next()
			print dictionary
			# print current.get_data()

# print ll.display()
# remove_duplicates(ll)

# 2.2 Find kth to last element in a linked list
def kth_element(self, k):
	p1 = self.head
	p2 = self.head
	shift = k

	while(shift > 0):
		p1 = p1.get_next()
		shift -=1
		
	while(p1 != None):		
		p1 = p1.get_next()
		p2 = p2.get_next()

	# print p2.get_data()
	return p2.get_data()

# kth_element(ll, 3)

# 2.3 Delete middle element of a linked list, given access to only that element
def delete_middle(self, m):
	current = m.get_next()
	m.data = current.get_data()
	m.set_next = current.get_next()

# 2.4 Partition a linked list around a value x s.t. all nodes before partition are lower, 
# and all nodes after partition are greater
def partition(self, x):
	ll1 = LinkedList()
	ll2 = LinkedList()
	current = self.head
	while current:
		if current.get_data() < x:
			ll1.insert(current.get_data())
			
		elif current.get_data >= x:
			ll2.insert(current.get_data())
		
		current = current.get_next()

	current = ll1.head
	while current:
		print current.get_data()
		# because inserts happen at the start of the linked list, we insert into ll2
		ll2.insert(current.get_data)
		current = current.get_next()
	
	print ll2.display()
	return ll2

# partition(ll, 5)

# 2.5 TODO
# 2.6 Given a circular linked list, return the node at the beginning of th loop TODO

# 2.7 Check if a linked list is a palindrome
# copy linked list to a new one using insert(which inserts at the start, hence it becomes a reverse copy)
def reverse_copy(l):
	reverse_ll = LinkedList()
	current = l.head
	while current:
		reverse_ll.insert(current.get_data())
		current = current.get_next()
	return reverse_ll


def palindrome_check(l):
	reverse_ll = reverse_copy(l)
	p1 = l.head
	p2 = reverse_ll.head

	for i in range(l.size()/2):
		if p1.get_data() != p2.get_data():
			print 'Not a palindrome.'
			return False
		else:
			p1 = p1.get_next()
			p2 = p2.get_next()
	print 'Linked list is a palindrome.'
	return True

ll2 = LinkedList()
data= [1,2,3,2,1]  
for i in data:
	ll2.insert(i)

print ll2.display()
palindrome_check(ll2)


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
			raise ValueError('Data no in linked list.')
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())


ll = LinkedList()
data= [1,2,3,4,5,6,6,4,3]  
for i in data:
	ll.insert(i)

print ll.display()
# print ll.size()
# print ll.search(2)

# Remove duplicates from an unsorted linked list
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

# Find kth to last element in a linked list
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

	print p2.get_data()
	return p2.get_data()

kth_element(ll, 3)





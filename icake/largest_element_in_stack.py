class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.items = []

	# T: O(1)
	def push(self, data):
		return self.items.append(data)
	
	# T: O(1)
	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def display(self):
		return self.items

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

class MaxStack(object):
	"""docstring for MaxStack"""
	def __init__(self):
		self.stack = Stack()
		self.max_stack = Stack()

	def push(self, item):
		self.stack.push(item)
		if data > self.max_stack.peek():
			self.max_stack.push(data)

	def pop(self):
		data = self.stack.pop()
		if data == self.max_stack.peek():
			self.max_stack.pop()
		return data

	def get_max(self):
		return self.max_stack.peek()		
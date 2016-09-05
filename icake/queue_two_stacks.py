# Implement a queue using 2 stacks
class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.items = []

	def push(self, data):
		return self.items.append(data)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(items) - 1]

	def display(self):
		return self.items

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

class Queue2Stacks(object):
	"""docstring for Queue2Stacks"""
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def enqueue(self, data):
		return self.s1.push(data)

	def dequeue(self):
		for i in xrange(self.s1.size()):
			self.s2.push(self.s1.pop())
		return self.s2.pop()
	
	def display(self):
		print self.s1.items
		print self.s2.items

	def realign(self):
		for i in xrange(self.s2.size()):
			self.s1.push(self.s2.pop())

q = Queue2Stacks()
data = [4,3,5,2]
for i in data:
	q.enqueue(i)

print q.display()
q.dequeue()
q.realign()
print q.display()
				
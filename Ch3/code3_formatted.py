# Basic implementation of stack
class stack(object):
	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)

	def push(self, data):
		return self.items.append(data)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def isEmpty(self):
		return self.items == []

	def display(self):
		l = len(self.items)
		print l   

# data = [1,2,3,4,5,6]  
# s = stack()  
# for i in data: 
#   s.push(i)

# Testing stack 
# print s.peek()
# print s.display()
# s.pop()
# print s.display()

# 3.1 Use a single array to implement 3 stacks
# TODO

# 3.2 Return the minimum element in the stack(design stack such)
# class StackMin(object):
# 	def __init__(self):
# 		self.items = []
# 		self.minimum = []

# 	def push(self, data):
# 		self.items.append(data)
# 		# checking if data is lower than minimum value
# 		if len(self.minimum) == 0 or data <= self.minimum[-1]:
# 			self.minimum.append(data)

# 	def pop(self):
# 		if len(self.items) == 0:
# 			return None
# 		data = self.items.pop()
# 		# if data to be popped is the lowest value in the minimum list
# 		if data == self.minimum[-1]:
# 			self.minimum.pop()
# 		return data

#     def get_min(self):
#     	if len(self.minimum) == 0:
#     		return None
#     	return self.minimum[-1]



class StackMin(object):
	def __init__(self):
		self.items = []
		self.minimum = []

	def push(self, data):
		print data
		self.items.append(data)
		print self.items
		if len(self.minimum) == 0:
			self.minimum.append(data)
		elif data <= self.minimum[-1]:
			self.minimum.append(data)
		print self.minimum
		

	def pop(self):
		if len(self.items) == 0:
			return None
		popped_data = self.items.pop()
		if popped_data == self.minimum[-1]:
			self.minimum.pop()
		return popped_data

	def get_min(self):
		min_value = self.minimum[-1]
		if len(self.minimum) == 0:
			return None 
		return min_value
			

# data = [4,3,9,2]
# s = StackMin()
# for i in data:
# 	s.push(i)

# 3.3 Implement SetOfStacks which comprises of several stacks and should create a new stack when a previous one reaches
# capacity.
class StackOfStacks(object):
	"""docstring for StackOfStacks"""
	def __init__(self, capacity):
		self.sos = [[]]
		self.capacity = capacity

	def __str__(self):
		for i in self.sos:
			print i
		return ''

	def push(self, data):
		if len(self.sos[-1]) >= self.capacity:
			self.sos.append([])
		self.sos[-1].append([data])

	def pop(self):
		if len(self.sos[-1]) != []:
			popped_data = self.sos[-1].pop()
		elif len(self.sos[-1]) == []:
			return None
		return popped_data

	def pop_at_index(self, index):
		return self.sos[index-1].pop()

# s = StackOfStacks(3)
# data = [[4,5], [3,8,7], 9, 10]
# for i in data:
# 	s.push(i)
# print s
# s.pop()
# print '\n'
# print s
# s.pop_at_index(1)
# print s
	
# 3.4 Tower of Hanoi problem
def hanoi(n, source, aux, target):
	if n >= 1:
		print 'n', n
		# we move all but the bottom disk on the source to an aux
		hanoi(n-1, source, aux, target)
		# print '		move 1'
		# print 'source: ',source
		# print 'aux: ', aux
		# print 'target: ',target

		# move all the blocks from aux to target(on top of largest block)
		hanoi(n-1, aux, target, source)
		# print '		move 2'
		# print 'source: ', source
		# print 'aux: ', aux
		# print 'target: ', target

# hanoi(5,'A', 'B', 'C')

# 3.5 Implement a queue using 2 stacks
class Queue2Stack(object):
	"""docstring for Queue2Stack"""
	def __init__(self):
		self.s1 = stack()
		self.s2 = stack()

	def enqueue(self, data):
		self.s1.push(data)

	def dequeue(self):
		if self.s2.isEmpty():
			for i in range(self.s1.size()):
				self.s2.push(self.s1.pop())
		# print 's2: ',self.s2.items
		# print self.s2.pop()
		return self.s2.pop()

	def realign(self):
		for i in range(self.s2.size()):
			self.s1.push(self.s2.pop())


	def display(self):
		print 's1: ', self.s1.items
		print 's2: ', self.s2.items

# q = Queue2Stack()
# data = [4,3,7,2]
# for i in data:
# 	q.enqueue(i)
# print 'Q: \n', q.display()
# print 'Removed element: ', q.dequeue()
# print 'Q: \n', q.display()
# q.realign()
# print 'Realigned Q: \n', q.display()

# 3.6 Sort a stack ascending order(largest items on top) 
# TODO
def stack_sort(s):
	ts = stack()
	while not s.isEmpty():
		temp = s.pop()
		print 'temp: ', temp
		
		while not ts.isEmpty() and ts.peek() > temp:
			s.push(ts.pop())
			print '		check 1 - s: ', s.items
		
		ts.push(temp)
		print 'ts: ', ts.items
		
		while not s.isEmpty and s.peek() >= ts.peek():
			ts.push(s.pop())
			print '		check 2 - ts: ', ts.items

		print '				s:',s.items
		print '				ts:',ts.items
		print '				*** next iteration ***'
	return ts

# data = [4,2,1,3,5]  
# s = stack()  
# for i in data: 
#   s.push(i)
# print s.items
# s = stack_sort(s)
# print s.items
			


# 3.7 Variation of Q using 2 stacks 
# TODO
class CatDog(object):

	def __init__(self):
		self.s_cat = stack()
		self.s_dog = stack()

	def enqueue(self, type, data):
		if type == 'cat':
			return self.s_cat.push(data)
		else :
			return self.s_dog.push(data)

	def deq_dogs(self):
		return self.s_dog.pop()

	def deq_cats(self):
		return self.s_cat.pop()


	def dequeany(self): 
		#print self.s_dog.peek()[1]

		if self.s_dog.peek()[1] < self.s_cat.peek()[1]:
			return self.s_dog.pop()
		else :
			return self.s_cat.pop()

	def display(self):
		print self.s_cat.items()
		print self.s_dog.items()

# q = CatDog()
# q.enqueue('cat', 1)
# q.display()


# Alternative solution to sorting a stack
def sortstack(s):  
      tempstack = stack()  
      temp = None  
      for i in range((s.size())):  
           temp = s.pop()  
           print 'temp: ', temp
           count = 0  
           for j in range((tempstack.size())):  
                if tempstack.peek() > temp:  
                     s.push(tempstack.pop()) 
                     print 's: ', s.items 
                     count += 1  
                else:  
                     break  
           tempstack.push(temp) 

           print 'tempstack: ', tempstack.items 
           
           for j in range(count):  
                tempstack.push(s.pop())
      print 'tempstack: ', tempstack.items 
      return tempstack  

data = [4,2,1,3,5]  
s = stack()  
for i in data: 
  s.push(i)
print 'Original stack: ', s.items
s = sortstack(s)


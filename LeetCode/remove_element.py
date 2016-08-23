# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Time:  O(n)
# Space: O(1)

class RemoveElement(object):
	"""docstring for RemoveElement"""
	def remove_element(self, l, elem):
		i = 0
		last = len(l) - 1
		while i <= last:
			if l[i] == elem:
				l[i] = l[last]
				l[last] = l[i]
				last -= 1
			else:
				i += 1
		return last + 1

if __name__ == '__main__':
	print RemoveElement().remove_element([3,5,2,6,1,2,3], 2)
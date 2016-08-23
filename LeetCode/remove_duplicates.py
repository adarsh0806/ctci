# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array A = [1,1,2],
# 
# Your function should return length = 2, and A is now [1,2].
# Time:  O(n)
# Space: O(1)

class RemoveDuplicates(object):
	"""docstring for RemoveDuplicates"""
	def remove_duplicates(self, l):
		i = 0
		for j in range(1, len(l)):
			if l[i] != l[j]:
				i += 1
				# TODO this step: explanation
				l[i] = l[j]
		return i + 1

if __name__ == '__main__':
	print RemoveDuplicates().remove_duplicates([1,1,2])
			
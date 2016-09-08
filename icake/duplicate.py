# S: O(n), T:O(n)
def find_duplicates(l):
	l_set = set()
	duplicates = []
	for i in l:
		if i in l_set:
			duplicates.append(i)
		else:
			l_set.add(i)
	return duplicates

print find_duplicates([3,2,4,5,2,6,6])

# optimized for space
# TODO
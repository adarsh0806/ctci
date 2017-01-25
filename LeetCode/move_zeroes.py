'''
Move the 0s in a list to the end of the list
'''
def move_zeroes(l):
	i, j = 0, 0
	while i < len(l):
		if l[i] != 0:
			l[i], l[j] = l[j], l[i]
			j += 1
		i += 1
	return l

print move_zeroes([0,4,5,2,0,7,9])
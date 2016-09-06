def reverse_string(s):
	s = list(s)
	s = s[::-1]
	s = ''.join(s)
	return s

# print reverse_string('hello')
# T: O(n), S: O(1)
def reverse_string(s):
	s = list(s)
	# left pointer
	l = 0
	# right pointer
	r = len(s) - 1
	while l < r:
		s[l], s[r] = s[r], s[l]
		l += 1
		r -= 1
	return ''.join(s)

print reverse_string('hello')

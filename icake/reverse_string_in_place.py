def reverse_string(s):
	s = list(s)
	s = s[::-1]
	s = ''.join(s)
	return s

# print reverse_string('hello')

def reverse_string(s):
	s = list(s)
	l = 0
	r = len(s) - 1
	while l < r:
		s[l], s[r] = s[r], s[l]
		l += 1
		r -= 1
	return ''.join(s)

print reverse_string('hello')

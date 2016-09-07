# icake solution implements Counter and string methods manually. TODO
def word_cloud(s):
	from collections import Counter
	import string
	s = s.lower()
	s = s.translate(string.maketrans('',''), string.punctuation)
	s = s.split(' ')
	c = Counter(s)
	return c

print word_cloud('After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.')
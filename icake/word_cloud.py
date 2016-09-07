# icake solution implements Counter and string methods manually. TODO
from collections import Counter
import string
def word_cloud(s):
	return Counter(s.translate(string.maketrans('',''), string.punctuation).lower().split(' '))

print word_cloud('After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.')
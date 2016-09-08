# implement collections' Counter method
from collections import defaultdict
def counter(s):
	dic = defaultdict(int)
	s = list(s)
	for char in s:
		dic[char] += 1
	return dict(dic)

# print counter('hello hows it going')


# implement collections' Counter method without using defaultdict
def counter(s):
	dic = {}
	s = list(s)
	for char in s:
		if char in dic:
			dic[char] += 1
		else:
			dic[char] = 1
	return dict(dic)

print counter('hey there, nice day today')
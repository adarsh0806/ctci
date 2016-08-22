"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.
Elements in a triplet (a,b,c) must be in ascending order. (ie, a <= b <= c)
"""
def three_sum(l):
	l = sorted(l)
	ans = []
	for i in range(0,len(l)-2):
		j = i + 1
		length = len(l) - 1
		while j > i and j < length:
			s = l[i] + l[length] + l[j]
			if s == 0:
				triplet = [l[i], l[length], l[j]]
				ans.append(triplet)
				j = j + 1
			elif s > 0:
				length = length - 1
			elif s < 0:
				j = j + 1

	# print ans
	# return answer in the form of a tuple
	print set(map(tuple, ans))
			
print three_sum([2,0,-1,-1,-2,3])

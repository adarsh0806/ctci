# Given an array S of n integers, 
# find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def three_sum_closest(l, target):
	l = sorted(l)
	result = l[0] + l[1] + l[2]
	for i in range(0,len(l) - 2):
		j = i + 1
		length = len(l) - 1
		while j < length:
			s = l[i] + l[j] + l[length]
			if s == target:
				return s
			# difference lies here between 3sum and 3sumclosest
			if abs(s - target) < abs(target - result):
				result = s
			elif s < target:
				j += 1
			else:
				length -= 1

	return s

print three_sum_closest([3,0,-1,-1,-2], 5)
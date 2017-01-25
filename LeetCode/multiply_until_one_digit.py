'''
Write a python function that keeps multiplying the digits of a number until the multiplication results in just 1 digit.

Return the number of times this multiplication needs to be done to achieve this result
'''
import operator

def mul_digits_one(n):
	count = 0
	while n >= 10:
		n = reduce(operator.mul, [int(i) for i in str(n)], 1)
		count += 1
	return count

print mul_digits_one(452)

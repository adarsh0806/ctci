# top down
# T: O(n), S: O(n)
def td_fibonacci(n):
	if n == 1:
		return 1
	else:
		return n * td_fibonacci(n-1)

print td_fibonacci(5)

# bottom up
# T: O(n), S: O(1)
def bu_fibonacci(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result

print bu_fibonacci(5)

# TODO
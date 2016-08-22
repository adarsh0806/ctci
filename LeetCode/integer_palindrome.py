"""
Determine whether an integer is a palindrome. Implement a version w/o using any extra space as well.
"""
def integer_palindrome(n):
	l1 = [i for i in str(n)]
	l2 = l1[::-1]
	x1, x2 = [],[]
	for i in range(len(l1)/2):
		x1.append(l1[i])
		x2.append(l2[i])	
	x1 = int(''.join(x1))
	x2 = int(''.join(x2))
	if x1 == x2:
		return 'Palindrome.'
	else:
		return 'Not palindrome.'

# print integer_palindrome(1221)
# print integer_palindrome(1234521)
# print integer_palindrome(12345)

# Same problem with extra caveat of not using any extra space
def integer_pal(n):
	reverse = 0
	n1 = n
	while n1 > 0:
		reverse = reverse * 10 + n1 % 10
		n1 = n1 / 10
	print reverse
	return reverse == n

print integer_pal(1221)

def palindrome_check(s):
	return s == s[::-1]
# print palindrome_check('anna')

# check if any permutation of a string is a palindrome
def permutation_palindrome(s):
	chars = set()
	for i in s:
		if i not in chars:
			chars.add(i)
		else:
			chars.remove(i)
	return len(chars) <= 1
print permutation_palindrome('annam')
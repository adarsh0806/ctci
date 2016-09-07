# Return all possible permutations of a string
# T: O(n), S: (n)
def string_permutations(s):
	if len(s) <= 1:
		return set([s])
	all_chars_except_last = s[:-1]
	last_char = s[-1]
	perms_except_last = string_permutations(all_chars_except_last)
	perms = set()
	for i in perms_except_last:
		for j in xrange(len(all_chars_except_last) + 1):
			p = i[:j] + last_char + i[j:]
			perms.add(p)
	return perms

print string_permutations('cats')

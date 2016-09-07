# Return all possible permutations of a string
# T: O(n), S: (n)
def string_permutations(s):
	if len(s) <= 1:
		return set([s])
	# 'cat'
	all_chars_except_last = s[:-1]
	# 's'
	last_char = s[-1]
	# recursive call to generate all permutations of 'cat'
	perms_except_last = string_permutations(all_chars_except_last)
	# final solution set
	perms = set()
	# iterate through each permutation of 'cat'
	for i in perms_except_last:
		# go through each alphabet of 'cat'
		for j in xrange(len(all_chars_except_last) + 1):
			p = i[:j] + last_char + i[j:]
			# add to set
			perms.add(p)
	return perms

print string_permutations('cats')

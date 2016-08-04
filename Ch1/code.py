# Part 1: Data Structures
# Chapter 1: Arrays and Strings
# Check if string has all unique characters
def no_duplicates(stri):
    """ Determine if str_ has all unique characters """
    print len(stri) == len(set(stri))

# Testing
# no_duplicates('helo')
# no_duplicates('hello')

# Reverse a string
def reverse_string(stri):
	stri = list(stri)
	stri = stri[::-1]
	print ''.join(stri)
# Testing
# reverse_string('adarsh')

# Check if a string is a permutation of another
# Below are the permutations of string ABC.
# ABC ACB BAC BCA CBA CAB
def check_permuatation(s1, s2):
	s1 = list(s1)
	# Timsort(derived from merge sort and insertion sort): time complexity O(nlogn)
	s1 = sorted(s1)
	s2 = list(s2)
	s2 = sorted(s2)
	if s1 == s2:
		print 'Permutation.'
	else:
		print 'Not a permutation.'
# Testing
# check_permuatation('ZYX','CBA')
# check_permuatation('ABC','CBA')

# Replace all spaces in a string with %20

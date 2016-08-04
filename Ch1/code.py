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
def replace_spaces(s1):
	s1 = s1.split(' ')
	s1 = '%20'.join(s1)
	print s1
# Testing
# replace_spaces('mr john smith ')
# replace_spaces(' Hi there, how are you?')

# Perform string compression: aabbbccc becomes a2b3c3, if resulting string is not smaller than original, return original
def string_compression(s1):
	# Assuming no spaces in the string
	s2 = set(s1)
	s2 = sorted(s2)
	c = []
	for i in s2:
		c.append(s1.count(i))

	zipped = zip(s2,c)	
	concatenated_tuples = [j for i in zipped for j in i]	

	if len(concatenated_tuples) > len(s1):
		print s1
	else:
		print concatenated_tuples

# string_compression('aabbbbckkk')
# string_compression('zzyxtttc')


# Rotate a MxN matrix by 90 degrees (last row becomes the first column and so on)
##M by N matrix has dimensions 4 by 4
##Visual representation of contents:
##[ 1  2  3  4 ]
##[ 5  6  7  8 ]
##[ 9  10  11  12 ]
##[ 13  14  15  16 ]
##
##Visual representation of contents after rotating 90 degrees clockwise:
##[ 13  9  5  1 ]
##[ 14  10  6  2 ]
##[ 15  11  7  3 ]
##[ 16  12  8  4 ]
# TODO

# If an element in an MxN matrix is 0, it's row and column are set to 0
def update_matrix(matrix):
	zero_rows = {}
	zero_columns = {}
	for i, r_values in enumerate(matrix):
		print 'row = ',i
		for j, c_value in enumerate(r_values):
			print '  column = ',j
			print '    value = ', c_value
			if c_value == 0:
				zero_rows[i] = True
				zero_columns[j] = True

	print zero_rows
	print zero_columns
				
	for i, r_values in enumerate(matrix):
		for j, c_value in enumerate(r_values):
			if i in zero_rows or j in zero_columns:
				matrix[i][j] = 0

	print matrix
# Testing
# matrix1 = [[1,2,3],[4,0,6],[7,8,9]]
# matrix2 = [[1,2,3],[4,5,6],[7,8,0]]
# update_matrix(matrix1)
# update_matrix(matrix2)

# Check if a word is a substring of another word
def check_substring(s1, s2):
	if s2 in s1:
		print 'True'
	else:
		print 'False'

# check_substring('hellomoto', 'lomo')

# Check if word is a rotation of another word
def check_rotation(s1, s2):
	s3 = s2 + s2
	if s1 in s3:
		print True
	else:
		print False


check_rotation('apple', 'pleap')
check_rotation('apple', 'papel')


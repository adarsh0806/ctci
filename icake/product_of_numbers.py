# Brute Force
# class IntegerMult(object):
# 	"""docstring for IntegerMult"""
# 	def brute_force(self, l):
# 		soln = []
# 		for index, value in enumerate(l):
# 			for nested_index,nested_value in enumerate(l):
# 				if index != nested_index:
# 					soln.append(value * nested_value)				
# 		return set(soln)

# if __name__ == '__main__':
# 	print IntegerMult().brute_force([4,3,7])

# ICake Product before index
# l = [3,4,2,5,6,9,7]
# products_of_all_ints_before_index = [None] * len(l)

# product_so_far = 1
# for i in xrange(len(l)):
# 	products_of_all_ints_before_index[i] = product_so_far
# 	product_so_far = product_so_far * l[i]

# print products_of_all_ints_before_index
# print product_so_far 

def product_of_numbers_not_at_index(l):
	# Product before index
	products_of_all_ints_before_index = [None] * len(l)
	product_so_far = 1
	for i in xrange(len(l)):
		if i == 0:
			products_of_all_ints_before_index[i] = 1
			continue
		product_so_far *= l[i-1]
		products_of_all_ints_before_index[i] = product_so_far

	# Product after index
	product_after_index = [None] * len(l)
	product_so_far = 1
	for i in reversed(xrange(len(l))):
		if i == (len(l)-1):
			product_after_index[i] = 1
		else:
			product_so_far *= l[i+1]
			product_after_index[i] = product_so_far

	final_answer = [x*y for x,y in zip(products_of_all_ints_before_index, product_after_index)]
	return final_answer

l = [3,5,4,7]
print product_of_numbers_not_at_indice(l)
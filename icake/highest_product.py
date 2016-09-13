# T: O(nlgn)
# Does not account for negative values in the list
def highest_product(l):
	l_sorted = sorted(l, reverse = True)
	return l_sorted[0] * l_sorted[1] * l_sorted[2]

print highest_product([1,4,7,2])

# T: O(n), S: O(1) additonal
# Assuming at least 3 elements in list
def highest_product(l):
	# variable definitions
	highest = max(l[0], l[1])
	lowest = min(l[0],l[1])
	highest_product_two_nos = l[0] * l[1]
	lowest_product_two_nos = l[0] * l[1]
	highest_product_three_nos = l[0] * l[1] * l[2]
	# start from the third element
	for current in l[2:]:
		highest_product_three_nos = max(highest_product_three_nos, current * highest_product_two_nos, current * lowest_product_two_nos)
		highest_product_two_nos = max(highest_product_two_nos, current * highest, current * lowest)
		lowest_product_two_nos = min(lowest_product_two_nos, current * highest, current * lowest)
		highest = max(highest, current)
		lowest = min(highest, current)

	return highest_product_three_nos

print highest_product([1,4,7,2])
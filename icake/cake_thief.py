# TODO
# unbounded knapsack problem
def max_bag_value(tuples, weight_capacity):
	# defining list with indices as weight capacity values and list item values as monetary values
	max_value_list = [0] * (weight_capacity + 1)
	# iterate through each weight capacity for bag
	for current_capacity, in xrange(weight_capacity + 1):
		current_max_val = 0
		# iterate over w,v values to be put into the bag
		for weight,value in tuples:
			# Error handling: if a cake weighs 0 and has a positive value the value of our duffel bag is infinite.
            # if (cake_weight == 0 and cake_value != 0):
            #     return float('inf')
			
			if weight < current_capacity:
				# maximum value using current item is that items value + 
				# whatever is the max value obtained with the left over capacity
				max_val_using_weight = value + max_value_list[current_capacity - weight]
				current_max_val = max(current_max_val, max_val_using_weight)
		# maximum value at each indice(weight) of bag
		current_max_val[current_capacity] = current_max_val

	return max_value_list[weight_capacity]

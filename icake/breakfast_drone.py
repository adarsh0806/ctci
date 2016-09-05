from collections import Counter
def breakfast_drone(l):
	print Counter(l) 

# breakfast_drone([4,4,5,5,6,6,7,8,8])

# using XOR
# T: O(n), S: O(1)
def breakfast_drone(id_list):
	unique_id = 0
	for c_id in id_list:
		unique_id ^= c_id
	return unique_id

print breakfast_drone([4,4,5,5,6,6,7,8,8])

# How do you know when bit manipulation might be the key to solving a problem? Here are some signs to watch out for:

# You want to multiply or divide by 2 (use a left shift to multiply by 2, right shift to divide by 2).
# You want to "cancel out" matching numbers (use XOR).
def bsearch(target, nums):
	floor = -1
	cieling = len(nums)
	while floor + 1 < cieling:
		distance = cieling - floor
		guess_index = floor + distance/2
		guess_value = nums[guess_index]
		if target > guess_value:
			floor = guess_index
		elif target < guess_value:
			cieling = guess_index
		elif target == guess_value:
			return True
	return False

print bsearch(5, [2,3,4,5,6])
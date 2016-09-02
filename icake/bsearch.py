def bsearch(target, nums):
	floor = -1
	cieling = len(nums)
	while floor + 1 < cieling:
		guess_index = (floor + cieling)/2
		guess_value = nums[guess_index]
		if target > guess_value:
			floor = guess_index
		elif target < guess_value:
			cieling = guess_index
		elif target = guess_value:
			return True
	return False

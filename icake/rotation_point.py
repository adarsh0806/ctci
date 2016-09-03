# T: O(lgn) S: O(1)
def rotation_point(words):
	first_word = words[0]
	floor = 0
	cieling = len(words) - 1
	while floor < cieling:
		guess_index = floor + (floor + cieling)/2
		if words[guess_index] > first_word:
			floor = guess_index
		else:
			cieling = guess_index

	if floor + 1 == cieling:
		return cieling

def shuffle_deck(h1, h2, s_d):
	h1_i = 0
	h2_i = 0
	h1_max_index = len(h1) - 1
	h2_max_index = len(h2) - 1
	for c in s_d:
		if c == h1_i and h1_i < h1_max_index:
			h1_i += 1
		elif c == h2_i and h2_i < h2_max_index:
			h2_i += 1
		else:
			return False
	return True
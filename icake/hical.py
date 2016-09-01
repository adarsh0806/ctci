# T: O(nlgn) S: O(n)
def hical(m):
	sorted_m = sorted(m)
	merged_m = [sorted_m[0]]
	# start from the second tuple in list, first tuple added to merged list(after sorting)
	for curr_m_s, curr_m_e in sorted_m[1:]:
		# assign pointer to last tuple in merged list
		last_m_s, last_m_e = merged_m[-1]
		# check if current start time is lower= to the end time of last tuple in merged list
		if curr_m_s <= last_m_e:
			merged_m[-1] = (last_m_s, max(last_m_e, curr_m_e))
		else:
			# append the current tuple to the merged final tuple
			merged_m.append((curr_m_s, curr_m_e))

	return merged_m


print hical([(2,4), (3,7), (9,11), (8,10)])
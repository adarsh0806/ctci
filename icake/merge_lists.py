def merge_lists(l1, l2):
	# list 1 index pointer
	l1_i = 0
	# liste 2 index pointer
	l2_i = 0
	# merged list size
	m_l_size = len(l1) + len(l2)
	m_l = [0] * (m_l_size)
	# merged list pointer
	m_i = 0
	while m_i < m_l_size:
		# flag for checking if we have reached end of lists l1 and l2
		l1_finished = l1_i >= len(l1)
		l2_finished = l2_i >= len(l2)
		# insert if value in l1 is lesser than value in l2 or if l2 is finished
		if not l1_finished and ((l1[l1_i] < l2[l2_i]) or l2_finished):
			m_l[m_i] = l1[l1_i]
			l1_i += 1
		else:
			m_l[m_i] = l2[l2_i]
			l2_i += 1
		m_i += 1
	return m_l

print merge_lists([2,4,6], [3,5,8])


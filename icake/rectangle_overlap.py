# T: O(1), S: O(1)
# range overlap
def point_overlap(p1, w1, p2, w2):
	# highest starting point
	h_s_p = max(p1,p2)
	# lowest ending point
	l_e_p = min(p1 + w1, p2 + w2)
	# No overlap case
	if h_s_p >= l_e_p:
		return (None, None)

	overlap_width = l_e_p - h_s_p
	return h_s_p, overlap_width

# rectangular overlap
def rectangular_overlap(r1, r2):
	x_overlap, overlap_width = point_overlap(r1['left_x'],
							  				 r1['width'],
							  				 r2['left_x'],
							  				 r2['width'])
	y_overlap, overlap_height = point_overlap(r1['bottom_y'],
							  				  r1['height'],
							  				  r2['bottom_y'],
							  				  r2['height'])

	# no overlap case
	if not overlap_width or not overlap_height:
		return None

	return {
	'left_x' : x_overlap,
	'bottom_y': y_overlap,
	'width': overlap_width,
	'height': overlap_height
	}
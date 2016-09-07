# def greatest(l):
# 	mx = 0
# 	for i in l:
# 		if i > mx:
# 			current_max = i
# 		mx = max(mx, current_max)
# 	return mx
# print greatest([4,5,3])

# sort a list in time faster than T:O(nlgn)
# counting sort
# T: O(n), S:O(n)
def top_scores(l, highest_score):
	# list will be as long as the highest possible score
	scores = [0] * (highest_score + 1)
	# index is the score, value is the count of the number of times that score appears 
	for score in l:
		scores[score] += 1
	sorted_scores = []

	for score_value, count in enumerate(scores):
		for t in range(count):
			sorted_scores.append(score_value)
	return sorted_scores

print top_scores([45,46,43,47,43,45,49],50)
	
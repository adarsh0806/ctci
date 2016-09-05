# Write a function that takes an integer flight_length (in minutes) 
# and a list of integers movie_lengths (in minutes) and 
# returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
# T: O(n), S: O(n)
def in_flight(flight_length, movie_lengths):
	dic = {}
	for i in range(len(movie_lengths)):
		val = movie_lengths[i]
		if flight_length - val in dic:
			print 'Indices of movies that have the needed runtimes: ', dic[flight_length - val], i
			return True
		dic[val] = i 

print in_flight(10, [2,4,5,6,3,9,1])

# practice 3sum(all combinations of 3 numbers in a list that sum to 0)
def three_sum(l):
	l = sorted(l)
	ans = []
	for i in range(0, len(l) - 2):
		j = i + 1
		length = len(l) - 1
		s = l[i] + l[j] + l[length]
		if s == 0:
			triplet = [l[i], l[j], l[length]]
			ans.append(triplet)
		elif s < 0:
			j = j + 1
		elif s > 0:
			length = length - 1

	print set(map(tuple, ans))

print three_sum([2,0,-1,-1,-2,3])

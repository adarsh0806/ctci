# Write a function that takes an integer flight_length (in minutes) 
# and a list of integers movie_lengths (in minutes) and 
# returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

def in_flight(flight_length, movie_lengths):
	dic = {}
	for i in range(len(movie_lengths)):
		val = movie_lengths[i]
		if flight_length - val in dic:
			print 'Indices of movies that have the needed runtimes: ', dic[flight_length - val], i
			return True
		dic[val] = i 

print in_flight(10, [2,4,5,6,3,9,1])

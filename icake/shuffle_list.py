# fisher-yates shuffle or knuth shuffle
# T: O(n), S:(1)
import random
def get_random(f,c):
	return random.randrange(f, c + 1)

def shuffle(l):
	last_index = len(l) - 1
	for i in xrange(0,len(l) - 1):
		random_choice_index = get_random(i, last_index)
		l[i], l[random_choice_index] = l[random_choice_index], l[i]
		return l

print shuffle([5,6,3,7])
# T: O(n) S: O(n)
def reverse_words(words):
	w_list = words.split(' ')
	l = 0
	r = len(w_list) - 1
	while l < r:
		w_list[l], w_list[r] = w_list[r], w_list[l]
		l += 1
		r -= 1
	return w_list

print reverse_words('hello there')
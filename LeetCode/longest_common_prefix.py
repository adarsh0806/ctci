# A function to find the longest common prefix string amongst an array of strings.
def longest_common_prefix(words):
	words = sorted(words)
	print words
	longest = words[0]
	for word in words[1:]:
		i = 0
		while i < len(word) and i < len(longest) and word[i] == longest[i]:
			i += 1
		return longest[:i]

# print longest_common_prefix(['abc', 'abdc', 'abdeg'])

# pythonic and elegant. zip takes up a lot of space
def longest_common_prefix(words):
    prefix = '';
    for i in zip(*words):   	
        bag = set(i)       
        if len(bag) == 1:
            prefix += bag.pop()            
        else:
            break
    return prefix

print longest_common_prefix(['abc', 'abdc', 'abdeg'])
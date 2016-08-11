"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
"""
# TODO
def lengthOfLongestSubstring(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            # update the res
            res = max(res, i-start)
            start = max(start, dic[ch]+1)
        dic[ch] = i
   
    return max(res, len(s)-start)

print lengthOfLongestSubstring('abcabcbb')
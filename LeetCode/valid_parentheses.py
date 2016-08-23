# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" 
# are all valid but "(]" and "([)]" are not.

def valid_parentheses(s):
	dic = {
	'}' : '{',
	']' : '[',
	')' : '('
	}
	stack = []
	for i in s:
		if i in dic.values():
			stack.append(i)
		elif i in dic.keys():
			if stack == [] or dic[i] != stack.pop():
				return False
	return stack == []

print valid_parentheses("()[]{}")
print valid_parentheses("()[]{")
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"( ( () ) )", 
"( () () )", 
"( () )()", 
"()( () )", 
"()()()"
"""
def generate_parentheses(n):
	result = []
	generate_parentheses_recursive(result, '', n, n)
	return result

def generate_parentheses_recursive(result, current, left, right):
	if left == 0 and right == 0:
		result.append(current)
	if left > 0:
		generate_parentheses_recursive(result, current + '(', left - 1, right)
	if left < right:
		generate_parentheses_recursive(result, current + ')', left, right - 1)

print generate_parentheses(3)
	
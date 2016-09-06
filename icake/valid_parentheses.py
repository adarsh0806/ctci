# T: O(n) S:(n)
def valid_parentheses(s):
	dic = {
	'}':'{',
	']':'[',
	')':'('
	}
	stack = []
	for i in s:
		if i in dic.values():
			stack.append(i)
			print stack
		elif i in dic.keys():
			if stack == [] or dic[i] != stack.pop():
				return False
	return stack == []

print valid_parentheses('[]{}()')
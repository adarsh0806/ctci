import random
def rand7():
	return random.randrange(0,7)

# print rand7()

def rand5():
	result = 6
	while result > 5:
		result = rand7
	return result
print rand5()		
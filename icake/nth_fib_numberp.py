def fibonacci(n):
	if n in [0,1]:
		return 1
	return n * fibonacci(n-1)

print fibonacci(5)
# TODO
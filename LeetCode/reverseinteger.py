# Reverse digits of an integer.
# 
# Example1: x = 123, return 321
# Example2: x = -123, return -321

def reverse_integer(n):
	sign = 1 if n > 0 else -1
	n *= sign
	n  = list(str(n))[::-1]	
	j = int(''.join(n))
	return sign * j

print reverse_integer(-534)

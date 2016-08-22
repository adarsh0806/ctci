# convert roman numeral to integer
dic = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToInt(s):
    result = 0
    p = 'I'
    for c in s[::-1]:
        if dic[c] < dic[p]:
        	result -= dic[c]
        else:
        	result += dic[c]
        p = c  
    return result


print romanToInt('XIV')
print romanToInt('XVII')
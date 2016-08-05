def high_and_low(numbers):
    numbers = numbers.split()
    l = []
    for i in numbers:
        i = int(i)
        l.append(i)
    sorted_l = sorted(l)
    low = sorted_l[:1]
    high = sorted_l[-1:]
    soln = high + low
    print type(soln)
    soln = ' '.join(str(i) for i in soln)
    print soln

# http://www.codewars.com/kata/evil-autocorrect-prank/train/python
import re
def autocorrect(input):
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)

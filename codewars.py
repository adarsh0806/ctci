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

# Morse code decoder
def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
    morse_to_word = {value:key for key,value in MORSE_CODE.items()}  
    decoded = [''.join(morse_to_word.get(i)) for i in morseCode.split()]
    join_decoded = ' '.join(decoded)
    
    # for word in morseCode.strip().split('   '):
    #     for letter in word.split(' '):
    #         print morse_to_word.get(letter)

    d =  ' '.join(''.join(morse_to_word.get(letter) for letter in word.split(' ')) for word in morseCode.strip().split('   '))
    print d

# decodeMorse('.... . -.--   .--- ..- -.. .')

# Longest common substring
def lcs(s1, s2):
    pass

# lcs('agbcadaaak', 'anbfcadhaaaj') # lcs is aaa

# Find the length of the longest substring in the given string s that is the same in reverse.
# TODO
def longest_palin(s):
    longest = 0
    for left in xrange(len(s)):
        for right in xrange(len(s), left, -1):
            if s[left:right] in (s[left:right])[::-1]:
                longest = max(right-left, longest)
                break
    return longest
    
# def longest_pal(s):
#     longest = 0
#     print len(s)
#     for left in range(len(s)):
#         print 'left: ', left
#         for right in range(len(s), left, -1):
#             print ' right: ', right
#             if s[left:right] in (s[left:right])[::-1]:
#                 print 's[left:right]: ', s[left:right]
#                 print '(s[left:right])[::-1]: ',(s[left:right])[::-1]
#                 longest = max(right-left, longest)
#                 print longest
#                 return 

# longest_pal('abaa')




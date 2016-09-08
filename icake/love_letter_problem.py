# Given a string L representing the letter and a string N representing the newspaper, return true if the L can be written entirely from N and false otherwise.
# T: O(n), S:(n)
from collections import Counter
def pramp(l,n):
   import string
   # l = l.translate(string.maketrans('',''), string.punctuation)
   l = l.replace(' ','')
   n = n.replace(' ','')
   newspaper = Counter(n)
   love_letter = Counter(l)
   for key, value in love_letter.iteritems():
   	if love_letter[key] <= newspaper[key]:
   		print 'the letter {} in love letter has sufficient chars.', format(key)
   	else:
   		print 'the letter {} in love letter does not have sufficient chars.', format(key)
   		
   
print pramp('i love you!', 'i love you so much.')
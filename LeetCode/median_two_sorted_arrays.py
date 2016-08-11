
# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall
# run time complexity should be O(log (m+n)).

import numpy as np 
a = sorted([4,3,6,2])
b = sorted([9,3,5])
# numpy median is O(nlogn)
c = sorted(a + b)
print c
print np.median(c)
# return indices of elements whose sum is equal to a target
def two_sum(data, target):
    dic = {}
    for i in range(len(data)):
        val = data[i]
        if (target - val) in dic:
            return dic[target - val], i
        dic[val] = i

print two_sum([2,4,1,3], 7)
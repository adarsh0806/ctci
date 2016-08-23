# Given a digit string, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 
# lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
def letterCombinations(digits):
        dic = {'1':'',
        	   '2':'abc',
        	   '3':'def',
        	   '4':'ghi',
        	   '5':'jkl',
        	   '6':'mno',
        	   '7':'pqrs',
        	   '8':'tuv',
        	   '9':'wxyz',
        	   '0':''}

        result = ['']
        for i in digits:
            result=[ j + k for j in result for k in dic[i]]
             
        return result

print letterCombinations('23')
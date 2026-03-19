import math

class Solution(object):
    def getPermutation(self, n, k):
        
        nums = [str(i) for i in range(1, n+1)]
        k -= 1  # convert to 0-based index
        
        result = ""
        
        for i in range(n, 0, -1):
            fact = math.factorial(i-1)
            
            index = k // fact
            result += nums[index]
            
            nums.pop(index)
            
            k %= fact
        
        return result
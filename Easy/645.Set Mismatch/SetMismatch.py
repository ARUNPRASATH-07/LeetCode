class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        c=[0]*(n+1)
        for num in nums:
            c[num]+=1
        d=m=-1
        for i in range(1,n+1):
            if c[i]==2:
                d=i
            if c[i]==0:
                m=i
        return [d,m]


        
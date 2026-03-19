class Solution(object):
    def permuteUnique(self, nums):
        res = []
        per = []
        nums.sort()

        def dfs(remain):

            if not remain:
                res.append(per[:])
                return
            for i in range(len(remain)):
                if i > 0 and remain[i] == remain[i -1]:continue
                per.append(remain[i])
                dfs(remain[:i] + remain[i+1:])
                per.pop()

        dfs(nums)
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
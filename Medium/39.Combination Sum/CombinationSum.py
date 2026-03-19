class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()   # 🔥 Step 1: sort for pruning
        result = []
    
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
        
            for i in range(start, len(candidates)):
                
                # 🔥 Early pruning
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # reuse allowed
                path.pop()
    
        backtrack(0, [], target)
        return result
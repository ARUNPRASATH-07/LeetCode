class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone = {
            "2":"abc", "3":"def", "4":"ghi",
            "5":"jkl", "6":"mno", "7":"pqrs",
            "8":"tuv", "9":"wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            
            # If combination length equals digits length
            if index == len(digits):
                res.append(path)
                return
            
            # Get letters for current digit
            letters = phone[digits[index]]
            
            for letter in letters:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        
        return res
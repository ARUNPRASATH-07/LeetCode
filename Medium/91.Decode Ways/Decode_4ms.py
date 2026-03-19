class Solution(object):
    def numDecodings(self, s):
        memo = {}

        def backtrack(index):
            # If we've processed the whole string, that's 1 successful decoding
            if index == len(s):
                return 1
            
            # If the current digit is '0', no valid letter starts with 0
            if s[index] == '0':
                return 0
            
            if index in memo:
                return memo[index]

            # Choice 1: Single digit (1-9)
            res = backtrack(index + 1)

            # Choice 2: Two digits (10-26)
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                res += backtrack(index + 2)

            memo[index] = res
            return res

        return backtrack(0)
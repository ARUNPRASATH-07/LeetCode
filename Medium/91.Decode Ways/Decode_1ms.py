class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        # Initial states
        prev2 = 1  # Equivalent to dp[0]
        prev1 = 1  # Equivalent to dp[1]
        
        for i in range(1, len(s)):
            current = 0
            
            # Choice 1: Single digit (s[i])
            if s[i] != '0':
                current += prev1
                
            # Choice 2: Two digits (s[i-1:i+1])
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
            
            # Slide the window!
            # YOUR TASK: 
            # Update prev2 and prev1 for the next iteration.
            # prev2 should become the old prev1
            # prev1 should become the current
            
            prev2 = prev1
            prev1 = current
            
        return prev1
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # If string is empty after whitespace
        if i == n:
            return 0

        # 2. Check sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Overflow check BEFORE adding digit
            if result > INT_MAX // 10 or \
               (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
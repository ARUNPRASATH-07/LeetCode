class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i, n = 0, len(s)

        # skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # sign
        sign = 1
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        num = 0
        while i < n and '0' <= s[i] <= '9':
            d = ord(s[i]) - 48

            # overflow check
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and d > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + d
            i += 1

        return sign * num
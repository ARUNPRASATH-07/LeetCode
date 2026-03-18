class Solution(object):
    def plusOne(self, digits):
        left = len(digits) - 1
        carry = 1   # because we add one
        
        while left >= 0:
            total = digits[left] + carry
            digits[left] = total % 10
            carry = total // 10
            
            if carry == 0:
                return digits
            
            left -= 1
        
        # if carry still remains
        digits.insert(0, 1)
        return digits
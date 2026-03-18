class Solution(object):
    def addBinary(self, a, b):
        la = len(a) - 1
        lb = len(b) - 1
        carry = 0
        result = []
        
        while la >= 0 or lb >= 0 or carry:
            total = carry
            
            if la >= 0:
                total += int(a[la])
                la -= 1
            
            if lb >= 0:
                total += int(b[lb])
                lb -= 1
            
            result.append(str(total % 2))   # binary digit
            carry = total // 2              # binary carry
        
        return "".join(result[::-1])
class Solution(object):
    def isNumber(self, s):
        num_seen = False
        dot_seen = False
        e_seen = False
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num_seen = True
            
            elif ch == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            
            elif ch == 'e' or ch == 'E':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False  # must see digit after e
            
            elif ch == '+' or ch == '-':
                if i != 0 and s[i-1] not in ['e', 'E']:
                    return False
            
            else:
                return False
        
        return num_seen
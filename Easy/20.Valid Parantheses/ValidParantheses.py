class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={')':"(","]":"[","}":"{"}
        l=[]
        for i in s:
            if i in "{([":
                l.append(i)
            else:
                if not l:
                    return False                
                if l[-1]!=d[i]:
                    return False
                l.pop()
        if not l:
            return True
        else:
            return False
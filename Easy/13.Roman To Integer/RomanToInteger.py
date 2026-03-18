class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        num=0
        i=0
        while i <len(s):
            if i+1 <len(s) and d[s[i]]<d[s[i+1]] :
                num+=d[s[i+1]]-d[s[i]]
                i+=2
            else:
                num+=d[s[i]]
                i+=1

        return num
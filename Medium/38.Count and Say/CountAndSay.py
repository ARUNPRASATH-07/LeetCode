class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s="1"
        if n==1: return s

        for _ in range(n-1):
            res=[]
            i=0
            while i < len(s):
                c=1
                while i+1<len(s) and s[i]==s[i+1]:
                    c+=1
                    i+=1
                res.append(str(c))
                res.append(s[i])
                i+=1
            s="".join(res)
        return s
    

        
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def backtrack(curstr,op,cl):
            if len(curstr)==2*n:
                res.append(curstr)
                return
            if op<n:
                backtrack(curstr+"(",op+1,cl)
            if cl<op:
                backtrack(curstr+")",op,cl+1)
        backtrack("",0,0)
        return res
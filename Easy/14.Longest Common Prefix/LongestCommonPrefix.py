class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str"""
        if not strs:
            return ""
        pre=strs[0]
        for  st in strs[1:]:
            while st.find(pre)!=0:
                pre=pre[:-1]
                if not pre:
                    return ""
        return pre




        
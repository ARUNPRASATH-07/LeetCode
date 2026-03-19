# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        l=[]
        if not root:
            return l
        def traverse(temp):
            if temp==None:
                return
            traverse(temp.left)
            l.append(temp.val)
            traverse(temp.right)
        traverse(root)
        return l
        
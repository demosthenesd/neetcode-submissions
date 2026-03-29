# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def sameTree (self,p,q):

        #check if both tree have None values, which makes them equal; hence true
        if p is None and q is None:
            return True
        #if only one of them is none, and other has values, not Equal; hence false
        if p is None or q is None:
            return False
        #obvs if values do not match if both are not none; not equal
        if p.val != q.val:
            return False
        
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot is None:
            return True

        if root is None:
            return False

        if self.sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)




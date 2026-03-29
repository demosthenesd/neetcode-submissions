# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(tree1,tree2):

            #essentially, if both trees are None, they equal
            if not tree1 and not tree2:
                return True
            
            #if one is none, but one has, then obvs not equal
            if not tree1 or not tree2:
                return False

            #self explanatory// if not equal, false
            if tree1.val != tree2.val:
                return False

            return dfs(tree1.right,tree2.right) and dfs(tree1.left, tree2.left)
        

        return dfs(p,q)


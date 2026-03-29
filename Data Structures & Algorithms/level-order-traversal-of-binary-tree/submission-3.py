# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        

        results = []
        queue = [root]


        while queue != []:

            next_queue = []
            level = []


            for item in queue:

                level.append(item.val)

                if item.left is not None:
                    next_queue.append(item.left)
                
                if item.right is not None:
                    next_queue.append(item.right)
            
            queue = next_queue
            results.append(level)

        return results
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []
        queue = [root]

        while queue:
            level = []
            next_queue = []

            for item in queue:
                level.append(item.val)

                if item.left is not None:
                    next_queue.append(item.left)

                if item.right is not None:
                    next_queue.append(item.right)

            results.append(level)
            queue = next_queue

        return results
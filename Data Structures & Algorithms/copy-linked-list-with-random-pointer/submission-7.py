"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copyObj = {None:None}

        copyHead = head

        while copyHead:

            copyObj[copyHead] = Node(copyHead.val)
            copyHead = copyHead.next

        
        copyHead = head

        while copyHead:

            copyObj[copyHead].next = copyObj[copyHead.next]
            copyObj[copyHead].random = copyObj[copyHead.random]

            copyHead = copyHead.next

        return copyObj[head]

        
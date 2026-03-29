# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # PHASE 1: Find the middle of the list
        # We use the Tortoise (slow) and Hare (fast) approach.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        # right_half_head starts after the middle
        right_half_head = slow.next
        slow.next = None # Sever the connection to create two separate lists

        # PHASE 2: Reverse the second (right) half
        # We need to flip 3 -> 4 into 4 -> 3
        prev_node = None
        current_node = right_half_head
        
        while current_node:
            next_hop = current_node.next  # Save the rest of the list
            current_node.next = prev_node # Flip the pointer backwards
            prev_node = current_node      # Move prev forward
            current_node = next_hop       # Move current forward
        
        # After the loop, 'prev_node' is the new head of the reversed half
        reversed_right_head = prev_node

        # PHASE 3: Merge the two halves (The "Zipper" Merge)
        # We weave them: Left1 -> Right1 -> Left2 -> Right2...
        left_ptr = head
        right_ptr = reversed_right_head

        while right_ptr:
            # Save the "next" steps for both lists so we don't lose them
            next_left = left_ptr.next
            next_right = right_ptr.next

            # Connect Left to Right
            left_ptr.next = right_ptr
            # Connect Right to the old Left.next
            right_ptr.next = next_left

            # Move our pointers forward for the next iteration
            left_ptr = next_left
            right_ptr = next_right
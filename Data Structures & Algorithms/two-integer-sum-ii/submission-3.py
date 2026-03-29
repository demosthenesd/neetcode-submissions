class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right] # Calculate sum of current pointers

            if current_sum == target:
                # Return 1-based indices as required by most versions of this problem
                return [left + 1, right + 1]
            
            elif current_sum > target:
                right -= 1 # Sum is too high, move right pointer inward to decrease it
            
            else: # current_sum < target
                left += 1  # Sum is too low, move left pointer inward to increase it
        
        return []

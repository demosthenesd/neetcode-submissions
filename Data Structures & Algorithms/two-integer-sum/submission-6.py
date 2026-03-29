class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        differences = {}

        for i in range(len(nums)):
            differences[nums[i]] = i 

        
        for j in range(len(nums)):
            diff = target - nums[j]

            if diff in differences and differences[diff] != j:
                return [j,differences[diff]]


        
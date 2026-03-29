class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        diff_set ={}

        for i in range (len(nums)):
            diff_set[nums[i]] = i;

        for j in range (len(nums)):
            res = target - nums[j]
            if res in diff_set and diff_set[res] != j:
                return [j, diff_set[res]]

        
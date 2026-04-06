class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for num in nums:

            res += [ out + [num] for out in res]
        
        return res
        
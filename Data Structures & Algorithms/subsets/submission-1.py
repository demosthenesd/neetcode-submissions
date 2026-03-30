class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for item in nums:

            res += [outputVal + [item] for outputVal in res]
        return res
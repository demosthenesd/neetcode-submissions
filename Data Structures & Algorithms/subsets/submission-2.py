class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for num in nums:

            res += [output + [num] for output in res]

        return res
        
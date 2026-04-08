class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

    
    # # Greg Hog solution

        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()

        return ans







    # #  Neetcode solution

    #     if len(nums)== 0:
    #         return [[]]
        
    #     perms = self.permute(nums[1:])
    #     res = []
    #     for p in perms:
    #         for i in range(len(p)+1):
    #             p_copy = p.copy()
    #             p_copy.insert(i,nums[0])
    #             res.append(p_copy)

    #     return res



        
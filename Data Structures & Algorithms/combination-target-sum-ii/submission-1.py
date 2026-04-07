class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        nums = candidates
        nums.sort()
        res = []

        def dfs(cur, start, target):
            if target == 0:
                res.append(cur)
                return

            for i in range(start,len(nums)):

                if i > start and nums[i] == nums[i-1]:
                    continue
                
                if nums[i] > target:
                    break
                
                dfs((cur +[nums[i]]), i+1, target - nums[i])
            
        dfs([],0,target)
        return res

        
























        # candidates.sort()
        # result = []

        # def comb(curr,start, target ):

        #     if target == 0:
        #         result.append(curr)
        #         return
            
        #     for i in range(start, len(candidates)):
        #         if i > start and candidates[i] == candidates[i-1]:
        #             continue
                
        #         if candidates[i] > target:
        #             break
        #         comb(curr+[candidates[i]], i+1, target-candidates[i])
        #     return
        
        # comb([],0,target)
        # return result


        
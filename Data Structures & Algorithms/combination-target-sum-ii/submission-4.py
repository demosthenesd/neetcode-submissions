class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        nums = candidates


        nums.sort()
        res = []


        def dfs(cur,start,target):


            if target == 0:
                res.append(cur)
                return

            for i in range(start, len(nums)):


                
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                if nums[i] > target:
                    break
                
            
                dfs((cur + [nums[i]]), i+1, target - nums[i])
        
        dfs([],0,target)

        return res


























        # nums = candidates
        # nums.sort()  # sort it first so easier to identify dupes later
        # res = []

        # def dfs(cur, start, target):
        #     #base case | check if target is met, append to result
        #     if target == 0:
        #         res.append(cur)
        #         return
            
        #     for i in range(start, len(nums)):
        #         # check if not the first choice, and is a dupe (SKIP)
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         # if current number is greater than target, IGNORE
        #         if nums[i] > target:
        #             break
               
               
        #         # recursively go through each number:
        #         # 1. add 1 each num to curr 
        #         # 2. increase i by 1
        #         # 3. substract target with current nums[i]
        #         dfs((cur + [nums[i]]), i+1, target - nums[i])
        
        # dfs([],0,target)
        # return res
















        # nums = candidates
        # nums.sort()
        # res = []

        # def dfs(cur, start, target):
        #     if target == 0:
        #         res.append(cur)
        #         return

        #     for i in range(start,len(nums)):

        #         if i > start and nums[i] == nums[i-1]:
        #             continue
                
        #         if nums[i] > target:
        #             break
                
        #         dfs((cur +[nums[i]]), i+1, target - nums[i])
            
        # dfs([],0,target)
        # return res

        
























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


        
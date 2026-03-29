class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        numSet = set(nums)

        longest = 0

        for i in nums:

            if(i-1 not in numSet):
                currentLength = 1
                currentNum = i
            
                while(currentNum +1) in numSet:
                    currentLength +=1
                    currentNum+=1

            
                longest = max(currentLength,longest)            



        return longest
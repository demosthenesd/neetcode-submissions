class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myMap = {}

        for i in range (len(nums)):
            myMap[nums[i]] = myMap.get(nums[i],0) + 1
        
        sortedVal = sorted(myMap,key=myMap.get,reverse=True)
        answer =[]
        for i in range(k):
            answer.append(sortedVal[i])


        print(answer)
        return answer

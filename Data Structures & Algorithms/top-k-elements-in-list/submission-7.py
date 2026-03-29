class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #long way of hashmap
        # counter = {}
        # for i in nums:
        #     counter[i] = counter.get(i,0) + 1

        # shortcut way of hashmap
        counter = Counter(nums)

        bucket=[]

        for _ in range(len(nums) + 1):
            bucket.append([])

        for key,val in counter.items():
            bucket[val].append(key)

        result = []

        k_count = k

        for i in range(len(bucket)-1,-1,-1):


            if not bucket[i]:
                continue

            for j in bucket[i]:
                result.append(j)
                k_count -= 1


            if k_count == 0:
                return result

            print(bucket[i])
        return result
        
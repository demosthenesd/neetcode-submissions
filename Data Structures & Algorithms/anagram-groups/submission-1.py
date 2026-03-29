class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #brute force i can think off. 
        #sort each string  so cat === act. then if string a == string b, group them in an inside array
        
        strs_sorted = []
        hashedMap = {}


        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))

            if sortedWord in hashedMap:
                hashedMap[sortedWord].append(strs[i])

            else:
                hashedMap[sortedWord] = [strs[i]]

        
        finalArray = []
        for key, val in hashedMap.items():
            finalArray.append(val)
        return finalArray

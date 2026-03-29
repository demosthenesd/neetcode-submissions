
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:



        # #brute force i can think off. 
        # #sort each string  so cat === act. then if string a == string b, group them in an inside array
        
        # strs_sorted = []
        # hashedMap = {}


        # for i in range(len(strs)):
        #     sortedWord = "".join(sorted(strs[i]))

        #     if sortedWord in hashedMap:
        #         hashedMap[sortedWord].append(strs[i])

        #     else:
        #         hashedMap[sortedWord] = [strs[i]]

        
        # finalArray = []
        # for key, val in hashedMap.items():
        #     finalArray.append(val)
        # return finalArray


        myMap = defaultdict(list)

        for word in strs:


            freq_counter = [0] * 26
            for chars in word:

                freq_counter[ord(chars) - ord('a')] += 1 

            updated_freq = tuple(freq_counter)
            myMap[updated_freq].append(word)
    

        answer = list(myMap.values())

        print(answer)

        return(answer)
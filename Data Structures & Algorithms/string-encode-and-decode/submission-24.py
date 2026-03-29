class Solution:

    # def encode(self, strs: List[str]) -> str:

    #     encodedString = ""

    #     for i in range(len(strs)):
    #         encodedString += strs[i] +  "|" 

    #     return encodedString
    # def decode(self, s: str) -> List[str]:

    #     result = s.split("|")
        
    #     result.pop()


    #     return result


    def encode(self, strs: List[str]) -> str:

        res = ''
        for word in strs:
            res += str(len(word)) + "|" + word
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        index = 0
        
        while index < len(s): 

            num_of_str = ''
        
            while s[index] != "|":
                num_of_str += s[index]
                index +=1
            
            if s[index] == "|":
                index +=1

            print(num_of_str)
            length = int(num_of_str)
            word = s[index:index + length]

            res.append(word)
            index += length


        return res




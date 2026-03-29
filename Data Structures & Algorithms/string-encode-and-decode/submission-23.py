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

        encodedString = ''
        for word in strs:
            encodedString += str(len(word)) + "|" + word 

        return encodedString


    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            num_of_str = ''

            while s[i] != "|":
                num_of_str += s[i]
                i += 1
            
            length = int(num_of_str)
            i += 1

            word = s[i:i+length]

            result.append(word)

            i+=length
        return result


            
                

                
                

            

            


        return []



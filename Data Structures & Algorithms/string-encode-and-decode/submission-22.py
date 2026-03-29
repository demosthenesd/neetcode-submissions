class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ""

        for i in range(len(strs)):
            encodedString += strs[i] +  "|" 

        return encodedString
    def decode(self, s: str) -> List[str]:

        result = s.split("|")
        
        result.pop()
        print(result)


        return result

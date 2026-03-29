class Solution:
    def isValid(self, s: str) -> bool:

        hm = {'}':'{',']':'[', ')': '('}
        stk = []

        for char in s:

            #check if a closing bracket
            if char in hm:
                
                #check if the stack is not empty
                #and if the top stack matches the bracket
                if stk and stk[-1] == hm[char]:
                    stk.pop()
                else:
                    return False

            #else if opening bracket            
            else:
                stk.append(char)

        
        return True if not stk else False




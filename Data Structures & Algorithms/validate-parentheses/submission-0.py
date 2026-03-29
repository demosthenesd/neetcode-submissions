class Solution:
    def isValid(self, s: str) -> bool:

        hm = {'}':'{',']':'[', ')': '('}
        stk = []


        for c in s:

            if c in hm:
                if stk and stk[-1] == hm[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        
        return True if not stk else False
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def gen(o,c,cur):

            if o == c == 0:
                res.append(cur)
                return
            
            if o > 0:
                gen(o-1,c,cur+"(")
            if o < c:
                gen(o,c-1,cur+")")
        gen(n,n,"")

        return res
        
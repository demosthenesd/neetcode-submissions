class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        res = 0

        for i in tokens:

            if i == "+":
                stk.append(int(stk.pop() + stk.pop()))
            elif i == "-":
                a,b = stk.pop(), stk.pop()
                stk.append(int(b-a))
            elif i == "/":
                a,b = stk.pop(), stk.pop()
                stk.append(int(b/a))

            elif i == "*":
                stk.append(int(stk.pop() * stk.pop()))
            else:
                stk.append(int(i))
        
        return stk[0]

            
        
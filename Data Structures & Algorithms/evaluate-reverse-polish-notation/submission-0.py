class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        opSet = {'+', '-', '/', '*'}
        stk = []

        res = 0

        for i in range(len(tokens)):

            # check if the item is an operator

            if stk and tokens[i] in opSet:
                val1 = int(stk.pop())
                val2 = int(stk.pop())

                if tokens[i] == '+': res = val2 + val1
                elif tokens[i] == '-': res = val2 - val1
                elif tokens[i] == '*': res = val2 * val1
                else: res = int(val2 / val1)
                
                stk.append(res)
            
            else:
                stk.append(tokens[i])


        return int(stk[0])
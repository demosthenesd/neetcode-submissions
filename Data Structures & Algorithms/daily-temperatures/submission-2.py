class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # will store [temp, index] for days waiting for a warmer day
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = index - prev_index

            stack.append([temp, index])

        return res

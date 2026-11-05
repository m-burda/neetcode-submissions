class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev = stack.pop()
                res[prev[0]] = i - prev[0]
            stack.append((i, temp))
        
        return res
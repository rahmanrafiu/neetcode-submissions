class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                val = stack.pop()
                res[val[1]] = i - val[1]
            stack.append(tuple([t, i]))
        
        return res
                
        
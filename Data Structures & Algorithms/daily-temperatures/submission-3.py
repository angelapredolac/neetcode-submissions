class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] # indices of possible warmer days

        for i in range(n-1, -1, -1):
            # remove days that are not warmer than today
            while (
                stack
                and temperatures[stack[-1]] <= temperatures[i]
            ):
                stack.pop()
            
            # top is now the closest warmer day
            if stack:
                result[i] = stack[-1] - i 
            
            stack.append(i)

        return result 

"""
stack = [28]
40 
while stack[-1]<curr:
    pop
    popped = [28]
    stack = []
    append 0
    stack = [28, 40]
35
while stack[-1]<curr:
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for rango in range(len(temperatures)):
            while stack and temperatures[rango] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = rango - prev

            stack.append(rango
            ) 
        return ans


    
        
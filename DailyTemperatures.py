'''
TC: O(n) - through all the inputs 
SC: O(n) - space to store the elements inside monotonic decresing stack
'''
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,i))
            elif temp <= stack[-1][0]:
                stack.append((temp,i))
            else:
                while stack and stack[-1][0]<temp:
                    t = stack.pop()
                    res[t[1]] = i-t[1]
                stack.append((temp,i))
        return res     
s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(s.dailyTemperatures([30,40,50,60]))
print(s.dailyTemperatures([30,60,90]))
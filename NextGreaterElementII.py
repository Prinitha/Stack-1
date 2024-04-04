'''
TC: O(3n) - O(n) - where we go through the length twice 
                    and pop elements out n times 
SC: O(n) - storing in monotonic decreasing stack
'''
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(0,2*n):
            i=i%n
            if not stack:
                stack.append((nums[i],i))
            else:
                if nums[i] <= stack[-1][0] and stack[-1][1]<i:
                    stack.append((nums[i],i))
                else:
                    while stack and nums[i] > stack[-1][0]:
                        popped = stack.pop()
                        res[popped[1]] = nums[i]
                    if not stack:
                        stack.append((nums[i],i))
                    elif nums[i] == stack[-1][0] and stack[-1][1]==i:
                        return res  
                    elif stack[-1][1]<i:
                        stack.append((nums[i],i))
s = Solution()
print(s.nextGreaterElements([10,3,1,0,18,5,4,4,6,1,11,6]))
print(s.nextGreaterElements([1,2,3,4,3]))
print(s.nextGreaterElements([1,2,1]))
print(s.nextGreaterElements([10,3,1,0,18,17,4,4,6,18,18,6]))
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, third = [], float('-inf')
        print(reversed(nums))
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False
sol = Solution()
nums = [3, 1, 4, 2]
result = sol.find132pattern(nums)
print(result)
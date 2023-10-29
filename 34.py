import bisect
from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1
        print(left)
        print(right)
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]
sol = Solution()
nums = []
target = 0
result = sol.searchRange(nums, target)
print(result)

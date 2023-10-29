from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while True:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        while nums[left] != target:
            left += 1
        while nums[right] != target:
            right -= 1
        return right - left + 1
sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = sol.searchRange(nums, target)
print(result)

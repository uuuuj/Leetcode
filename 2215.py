from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1= set(nums1)
        s2 = set(nums2)
        return [list(s1-s2), list(s2-s1)]
sol = Solution()
nums1 = [1,2,3]
nums2 = [2, 4, 6]
result = sol.findDifference(nums1, nums2)
print(result)
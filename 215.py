from typing import List
from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                if heap[0] <= num:
                    heappop(heap)
                    heappush(heap, num)
        return heap[0]
sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
result = sol.findKthLargest(nums, k)
print(result)
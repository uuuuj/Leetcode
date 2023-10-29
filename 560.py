from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        pref_sum = {0:1}
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in pref_sum:
                cnt += pref_sum[cur_sum - k]
            if cur_sum in pref_sum:
                pref_sum[cur_sum] += 1
            else:
                pref_sum[cur_sum] = 1
        return cnt


sol = Solution()
nums = [1 ,2, 3]
k = 3
result = sol.subarraySum(nums, k)
print(result)  # 예상 출력: 1

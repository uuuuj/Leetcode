from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        print(f"nums : {nums}")
        n = len(nums)
        dp = [1]*n
        print(f"dp : {dp}")
        for i in range(n):
            for j in range(i):
                print(f"i : {i}, j : {j}")
                print(f"nums[{i}] : {nums[i]}, nums[{j}] : {nums[j]}")
                print(f"dp[{i}] : {dp[i]}, dp[{j}]+1 : {dp[j]+1}")
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    print(f"dp : {dp}")
        print(f"최종 dp : {dp}")
        return max(dp)
sol = Solution()
nums = [10,9,2,5,3,7,101,18]
result = sol.lengthOfLIS(nums)
print(f"result : {result}")
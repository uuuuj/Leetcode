class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        char_set = set()
        max_len = 0
        for right in range(n):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_len = max(max_len, right - left + 1)
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(s[right])
        return max_len
sol = Solution()
s = "pwwkew"
result = sol.lengthOfLongestSubstring(s)
print(result)


from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range (len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                prev_end = merged[-1][1]
                cur_st = intervals[i][0]
                cur_end = intervals[i][1]
                if prev_end >= cur_st:
                    merged[-1][1] = max(prev_end, cur_end)
                else:
                    merged.append(intervals[i])
        return merged
sol = Solution()
intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
result = sol.merge(intervals)
print(result)
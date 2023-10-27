from typing import List
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for val in arr:
            try:
                counter[val] += 1
            except:
                counter[val] = 1
        arr = set(arr)
        arr = list(arr)
        arr = arr.sort()
        counter_val = sorted(counter.items(), key=lambda item: item[1])
        i = 0
        while k:
            counter_val[i][1] = counter_val[i][1] - 1
            arr.remove(arr[i])
            i += 1
            k -= 1
        return len(arr)



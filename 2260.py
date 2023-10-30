from typing import List
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #중복되는 카드가 없는 경우
        min_len = float('inf')
        dict_idx = {}
        for i, card in enumerate(cards):
            if card in dict_idx:
                min_len = min(min_len, i - dict_idx[card] + 1)
            dict_idx[card] = i
        if min_len == float('inf'):
            return -1
        return min_len
sol = Solution()
cards = [3,4,2,3,4,7]
result = sol.minimumCardPickup(cards)
print(result)
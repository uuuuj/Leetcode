class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # res = []
        # visited = [0 for i in range(len(number))]
        max_num = float('-inf')
        for i in range (len(number)):
            copy_number = list(number)
            # if number[i] == digit and not visited[i]:
            if number[i] == digit:
                # visited[i] = 1
                copy_number.pop(i)
                copy_number = ''.join(copy_number)
                max_num = max(max_num, int(copy_number))
        #         res.append(''.join(copy_number))
        # for i in range(len(res)):
        #     max_num = max(max_num, int(res[i]))
        max_num = str(max_num)
        return max_num
sol = Solution()
number = "1231"
digit = "1"
result = sol.removeDigit(number, digit)
print(result)

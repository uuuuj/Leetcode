from typing import List
from collections import deque
# n : course의 수
# prerequisites : 선수 과목
# prerequisites[i] = [a, b] : 과목 a를 수강하려면 먼저 과목 b를 수강해야 함을 나타낸다
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        #adj[선수과목] = [수강과목]
        adj = [[] for i in range(n)]
        indegree = [0] * n
        ans = []
        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1
        queue = deque()
        #선수과목이 없는 course는 queue에 미리 넣기
        #선수과목이 없는 course : indegree[course] == 0
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        print(queue)
        while queue:
            #진입 차수가 0인 과목들을 큐에 삽입(진입 차수가 0이어야 다음 노드로 이동 가능)
            cur = queue.popleft()
            ans.append(cur)
            #해당 원소와 연결된 노드들의 진입 차수에서 1빼기
            #cur == 선수 과목
            #adj[선수 과목] == 수강과목
            #next == 수강 과목
            for next in adj[cur]:
                indegree[next] -= 1
                #새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
                if indegree[next] == 0:
                    queue.append(next)
        return len(ans) == n

sol = Solution()
n = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]
result = sol.canFinish(n, prerequisites)
print(result)
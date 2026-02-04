"""

IDEA

 - BFS
 - 2x, x+1, x-1 case 고려

"""

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque([N])
MAX = 100001
visited = [-1] * MAX
visited[N] = 0

def bfs():

    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            return
        
        if 0<= x-1 < MAX and visited[x-1] == -1:
            visited[x-1] = visited[x] + 1
            q.append(x-1)

        if 0<= x+1 < MAX and visited[x+1] == -1:
            visited[x+1] = visited[x] + 1
            q.append(x+1)

        if 0<= 2*x < MAX and visited[2*x] == -1:
            visited[2*x] = visited[x] + 1
            q.append(2*x)


bfs()
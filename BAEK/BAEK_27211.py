"""

 - N, M 으로 나누면서 하면 될 거 같고
 - 0인거 하나 찾아서 bfs로 뭉탱이 하나 찾고
 - 다음 1 찾고 뭉탱이로 찾고 하면 될 거 같은데
 - 1을 어찌 찾지?

"""

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = (cx + dx[i]) % N
            ny = (cy + dy[i]) % M

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
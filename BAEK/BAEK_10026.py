import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True
    current_color = maps[x][y]

    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and maps[nx][ny] == current_color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

N = int(input())
maps = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt_normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt_normal += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if maps[i][j] == 'G':
            maps[i][j] = 'R'

cnt_blind = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt_blind += 1

print(cnt_normal, cnt_blind)
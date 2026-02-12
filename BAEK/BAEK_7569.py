"""
IDEA
 - 6 directions 방향으로 보면서 BFS 진행
 - 방문하지 않았고, 근접한 곳이라면 이전 값 + 1해서 진행
 - 1 시작이였으므로, 마지막에 =1 해서 결과값 출력
 - 
Time-Complexity
 - O(V+E) -> O(V)

structure
 - 3-dim List : graph

"""

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                q.append((z, y, x))

dz = [0,0,0,0,-1,1]
dy = [0,0,1,-1,0,0]
dx = [1,-1,0,0,0,0]

def bfs():

    while q:
        cz, cy, cx = q.popleft()
        
        for i in range(6):
            nz, ny, nx = cz+dz[i], cy+dy[i], cx+dx[i]
            if 0<= nz < H and 0<= ny < N and 0<= nx < M and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[cz][cy][cx] + 1
                q.append((nz, ny, nx))

    ans = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == 0:
                    print(-1)
                    return()
                
                ans = max(ans, graph[z][y][x])

    print(ans-1)
    return

bfs()
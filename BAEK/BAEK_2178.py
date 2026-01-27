"""
BAEK 2178 미로탐색

아아디어
 - bfs 활용

시간복잡도
 - 인접 list 사용하는 경우 O(V+E)
 - 인접 행렬 사용하는 경우 O(V^2)

자료구조
 - maze int[][]
 - directions int[]
"""

from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):

    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if nx <0 or nx >= N or ny<0 or ny>=M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N-1][M-1]

print(bfs(0,0))
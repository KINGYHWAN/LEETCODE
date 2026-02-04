"""

 - 시작점 기준으로 8방향 탐색(BFS)
 - condition 맞으면 append

"""


import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    I = int(input())
    maps = [[-1] * (I) for _ in range(I)]
    directions = [(2, 1), (1,2), (2,-1), (1, -2), (-1,-2), (-2, -1), (-2, 1), (-1, 2)]

    start_x, start_y = list(map(int, input().split()))
    end_x, end_y = list(map(int, input().split()))
    
    q = deque([(start_x, start_y)])
    maps[start_x][start_y] = 0 

    while q:

        x, y = q.popleft()

        if x == end_x and y == end_y:
            print(maps[x][y])
            return
        
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if 0<= new_x < I and 0 <= new_y < I and maps[new_x][new_y] == -1:
                maps[new_x][new_y] = maps[x][y] +1
                q.append((new_x, new_y))

t = int(input())
for _ in range(t):
    bfs()

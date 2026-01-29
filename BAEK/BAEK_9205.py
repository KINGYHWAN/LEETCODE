"""
IDEA
 - 출발점 기준으로 BFS로 갈 수 있는 편의점 파악 
 - 이동 후 편의점에서 갈 수 있으면 이동 후 최종적으로 도착지 도달 시 happy

Time Complexity
 - O(E^2)

Data Structure
 - store : N x 2
 - visited
 
"""

import sys
from collections import deque

input = sys.stdin.readline

def distance(p1, p2):
    
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def bfs():
    
    n = int(input())

    start = list(map(int, input().split()))

    stores = []

    for _ in range(n):
        stores.append(list(map(int, input().split())))
    
    end = list(map(int, input().split()))

    queue = deque([start])

    visited = [False] * n

    while queue:
        x, y = queue.popleft()

        if distance([x, y], end) <= 1000:
            print('happy')
            return
        
        for i in range(n):
            if distance([x, y], stores[i]) <= 1000 and visited[i] == False:
                visited[i] = True
                nx, ny = stores[i][0], stores[i][1]
                queue.append([nx, ny])

    print("sad")

t = int(input())

for _ in range(t):
    bfs()



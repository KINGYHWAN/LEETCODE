"""
IDEA
 - BFS 이용해서 물양 확인 (A, B)
 - 6개 direction에 대해서 진행하고 queue에 집어넣기

Time Coplexity
 - O(V)

Data structure
 - queue
 - 2-dim List

"""

import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

visited = [[False] * 201 for _ in range(201)]
ans = []

q = deque()
q.append((0,0))
visited[0][0] = True

def bfs():

    while q:
        curr_a, curr_b = q.popleft()
        curr_c = C - curr_a - curr_b

        if curr_a == 0:
            ans.append(curr_c)

        curr_water = [curr_a, curr_b, curr_c]
        limits = [A, B, C]

        for sender in range(3):
            for receiver in range(3):
                if sender == receiver:
                    continue

                water = min(curr_water[sender], limits[receiver] - curr_water[receiver])

                if water > 0:
                    next_water = list(curr_water)
                    next_water[sender] -= water
                    next_water[receiver] += water

                    next_a = next_water[0]
                    next_b = next_water[1]

                    if not visited[next_a][next_b]:
                        visited[next_a][next_b] = True
                        q.append((next_a, next_b))

bfs()
ans.sort()
print(*ans)


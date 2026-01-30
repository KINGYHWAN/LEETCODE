"""

IDEA
 - BFS
 - 해당 위치에서 점프 거리만큼 움직여서 1 ~ n 사이에 있는지 확인
 - 방문한 경우 True로 바꾸고 # of True 출력

Time Complexity
 - O(N)

data structure
 - jump : int []
"""

import sys
from collections import deque

import sys 
input = sys.stdin.readline

n = int(input())
Jump = list(map(int, input().split()))
start = int(input())


q = deque([start])
visited = [False] * (n+1)
visited[start] = True

while q:
    x = q.popleft()
    left, right = x - Jump[x-1], x + Jump[x-1]

    if 1 <= left <= n and visited[left] == False:
        visited[left] = True
        q.append(left)

    if 1 <= right <= n and visited[right] == False:
        visited[right] = True
        q.append(right)

print(sum(visited))

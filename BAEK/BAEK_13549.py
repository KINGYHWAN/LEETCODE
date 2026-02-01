"""

IDEA
 - 0-1 BFS로 진행, 가중치가 0인(0초) 2x 과정을 우선시 해서 진행
 - 2x 과정을 queue에 넣을 때 appendleft() 사용해서 우선적으로 진행
    -> 가중치가 작은 것을 우선으로 진행하는듯
    -> 최단거리 찾는 것이라 우선순위를 중요시 하는 듯

Time Complexity
 - O(E+V) -> O(4V) => O(V)

Structure
 - visited int []
 - deque

"""

import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, k):
    
    visited = [-1] * 100001

    q = deque([n])
    visited[n] = 0

    while q:
        x = q.popleft()
        if x == k:
            return visited[k]
        
        if 0<= 2*x < 100001 and visited[2*x] == -1:
            visited[2*x] = visited[x]
            q.appendleft(2*x)

        if 0<= x-1 < 100001 and visited[x-1] == -1:
            visited[x-1] = visited[x] + 1
            q.append(x-1)

        if 0<= x+1 < 100001 and visited[x+1] == -1:
            visited[x+1] = visited[x] + 1
            q.append(x+1)

n, k = map(int, input().split())

print(bfs(n,k))
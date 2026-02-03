import sys
input = sys.stdin.readline

from collections import deque

def bfs(F, S, G, U, D):

    visited = [-1] * (F+1)

    q= deque([S])
    visited[S] = 0

    while q:
        x = q.popleft()
        
        if x == G:
            print(visited[x])
            return
        
        if 1<= x + U <= F and visited[x+U] == -1:
            visited[x+U] = visited[x] + 1
            q.append(x+U)

        if 1<= x - D <= F and visited[x-D] == -1:
            visited[x-D] = visited[x] + 1
            q.append(x-D)

    print("use the stairs")

F, S, G, U, D = map(int, input().split())

bfs(F,S,G,U,D)

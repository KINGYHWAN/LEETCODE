"""

IDEA
 - board 판에 사다리/뱀 정보를 반영해서 구성 12 -> 98인 경우 board[12] = 98
 - 1 ~ 6 주사위 굴리면서 탐색

Time Complexity
 - O(V)

Structure
 - queue

"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [i for i in range(101)]
visited = [-1] * 101
for _ in range(N+M):
    u, v = map(int, input().split())
    board[u] = v

def bfs():
    q = deque([1])
    visited[1] = 0
    
    while q:
        x = q.popleft()

        if x == 100:
            return visited[100]
        
        for i in range(1, 7):
            next_x = x + i

            if next_x <= 100:
                target = board[next_x]

                if target <= 100 and visited[target] == -1:
                    visited[target] = visited[x] + 1
                    q.append(target)


print(bfs())
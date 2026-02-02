import sys
input = sys.stdin.readline

from collections import deque

def bfs(A, B):

    q = deque([(A, 1)])

    while q:
        current, count = q.popleft()

        if current == B:
            print(count)
            return
        
        if current *2 <= B:
            q.append((current*2, count+1))
        
        if current * 10 + 1 <= B:
            q.append((current*10+1, count+1))

    print(-1)

A, B = map(int, input().split())

bfs(A, B)
"""1926 problem

IDEA
 - 이중 for 문 이용해서 진행
 - BFS로 순환
 - 최대 크기 구하고 저장

time Complexity
 - O(V + E) -> vertex + edge
 - 1초당 1~2억번 연산 가능

Data Structure
 - Queue
 - map int[][]
 - check bool[][]

""" 
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(m)]

chk = [[False] * n for _ in range(m)]

cnt = 0
maxvalue = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    rs = 1
    q = [(i, j)]

    while q:
        i, j = q.pop()

        for k in range(4):
        
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < m and 0<= ny < n:
                if chk[nx][ny] == False and map[nx][ny] == 1:
                    rs += 1
                    chk[nx][ny] = True
                    q.append((nx, ny))

    return rs

for i in range(m):
    for j in range(n):
        if map[i][j] == 1 and chk[i][j] == False:
            cnt += 1
            chk[i][j] = True
            maxvalue = max(maxvalue, bfs(i, j))

print(cnt)
print(maxvalue)
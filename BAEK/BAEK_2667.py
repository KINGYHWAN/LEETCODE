"""

IDEA
 - Double for loop
 - visited x && value == 1 -> visit

TIme Complexity
 - DFS 
 - O(V+E) 

Data Structure
 - DFS : stack or recursive function
 - Recursive function


"""

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

results = []
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(i, j):

    global each
    each += 1

    for k in range(4):

        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if map[nx][ny] == 1 and chk[nx][ny] == False:
                chk[nx][ny] = True
                dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and chk[i][j] == False:
            cnt += 1
            each = 0
            chk[i][j] = True
            dfs(i, j)
            results.append(each)

print(cnt)
results.sort()
for i in results:
    print(i)


"""

IDEA
 - 간섭 : 인접 리스트 형태로 저장
 - 시작점부터 heap
 - while heap:
    방문 체크, 비용 추가, 간선 새롭게 추가

Time Complexity
 - MST -> O(ElogE) E ; edge

Structure
 - edge 저장(weight, near_edge)
 - 방문여부 bool[]
 - MST reulst int

"""

import sys, heapq

input = sys.stdin.readline

V, E = map(int, input().split())

edge = [[] for _ in range(V+1)] # 1 ~ V 쓸 수 있게 V+1개 definition
chk = [False] * (V+1)
rs = 0

for i in range(E):
    a, b, c = map(int, input().split())
    # bi-directional graph 
    edge[a].append([c, b])
    edge[b].append([c, a])

heap = [[0 , 1]] # (weight, vertex)

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)


print(rs)
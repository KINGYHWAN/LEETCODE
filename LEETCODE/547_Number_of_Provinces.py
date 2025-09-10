from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        connected = [False] * n
        province = 0

        for i in range(n):
            if not connected[i]:
                province += 1
                queue = deque([i])
                connected[i] = True
                while queue:
                    city = queue.popleft()
                    for j in range(n):
                        if isConnected[city][j] == 1 and not connected[j]:
                            connected[j] = True
                            queue.append(j)

        return province
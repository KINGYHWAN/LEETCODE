from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False] * len(rooms)
        queue = deque([0])
        visited[0] = True

        while queue:
            room = queue.popleft()

            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)

        return all(visited)


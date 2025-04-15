from collections import deque, defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        res = 0
        visited = set([0])
        queue = deque([0])

        while queue:
            city = queue.popleft()
            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res += cost
                    queue.append(neighbor)
        
        return res
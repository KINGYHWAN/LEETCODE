from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 그래프 구성: a / b = value에 대해 a->b 및 b->a 간선 추가
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        
        def bfs(start: str, end: str) -> float:
            # 시작 혹은 도착 노드가 그래프에 없으면 -1.0 반환
            if start not in graph or end not in graph:
                return -1.0
            
            # 시작 노드에서부터 탐색, (현재 노드, 누적 곱)
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                current, product = queue.popleft()
                # 도착한 경우 누적 곱을 반환
                if current == end:
                    return product
                for neighbor, value in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * value))
            return -1.0
        
        results = []
        for numerator, denominator in queries:
            results.append(bfs(numerator, denominator))
        return results

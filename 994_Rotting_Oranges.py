from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1) 초기화: 행·열 크기, 신선한(fresh) 개수, 초기 썩은 오렌지 좌표 큐에 담기
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # 2) BFS 탐색을 위한 방향 벡터
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # 3) 레벨 단위(분 단위)로 BFS 수행
        minutes = 0
        # fresh > 0 이고, 아직 전염시킬 수 있는 썩은 오렌지가 남아 있을 때만 반복
        while queue and fresh > 0:
            # 한 분 동안 처리할 큐 크기만큼 팝해서 이웃 전염 시도
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # 그리드 안이고, 신선(1)이면 전염
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2      # 썩은 상태로 변경
                        fresh -= 1           # 남은 신선 오렌지 수 감소
                        queue.append((nx, ny))
            minutes += 1  # 한 레벨(1분) 완료
        
        # 4) 모든 신선한 오렌지가 전염됐다면 minutes, 아니면 -1
        return minutes if fresh == 0 else -1

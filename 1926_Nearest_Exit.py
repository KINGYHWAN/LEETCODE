from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        
        ++.+
        ...+
        +++.    
        
        step이라는걸 이용해서 bfs를 몇 번 했는지 보면 되나 4방향에 대해 보고 .이면 넣고 +로 바꿔서 다신 못 넣게 하고
        exit면 그냥 멈춰버리고 step + 1 해서 반환하면 되지 않을까?
        
        """

        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

        rows, cols = len(maze), len(maze[0])
        x0, y0 = entrance

        queue = deque([(x0, y0, 0)])
        maze[x0][y0] = '+'

        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == '.':
                    if new_x in [0, rows - 1] or new_y in [0, cols-1]:
                        return steps+1
                    
                    maze[new_x][new_y] = '+'
                    queue.append((new_x, new_y, steps + 1))

        return -1
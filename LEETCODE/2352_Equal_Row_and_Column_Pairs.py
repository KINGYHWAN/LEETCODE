class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        
        row_list = grid
        col_list = []
        res = 0
        for i in range(len(grid[0])):
            temp = []
            for j in range(len(grid[0])):
                temp.append(grid[j][i])
            
            col_list.append(temp)
        
        print(col_list)
        for i in range(len(row_list)):
            for j in range(len(col_list)):
                if row_list[i] == col_list[j]:
                    res += 1
        
        return res
    
grid = [[3,2,1],[1,7,6],[2,7,7]]
a = Solution()
res = a.equalPairs(grid)
print(res)
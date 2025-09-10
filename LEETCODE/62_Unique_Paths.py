class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        first_row = [1] * n

        for _ in range(m-1):
            current_row = [1] * n
            for i in range(1, n):
                current_row[i] = current_row[i-1] + first_row[i]
            first_row = current_row
        
        return first_row[-1]

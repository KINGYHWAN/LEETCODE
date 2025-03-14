class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]

        pascal = [[1], [1, 1]]

        if numRows == 2:
            return pascal

        for i in range(2, numRows):  
            temp = []  # temp 초기화
            for j in range(len(pascal[i - 1]) - 1):  
                num = pascal[i - 1][j] + pascal[i - 1][j + 1]
                temp.append(num)

            temp = [1] + temp + [1]
            pascal.append(temp)

        return pascal

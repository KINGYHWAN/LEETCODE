class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        points.sort(key = lambda x : x[1])

        endpoint = points[0][1]
        arrows = 1

        for i in range(1, len(points)):

            start = points[i][0]
            end = points[i][1]
            
            if start <= endpoint <= end:
                continue
            else:
                arrows += 1
                endpoint = end
            

        return arrows
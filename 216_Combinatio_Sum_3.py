class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, target, k):
            if len(path) == k and target == 0:
                res.append(path)
                return 
            if len(path) > k or target < 0:
                return 
            for i in range(start, 10):
                backtrack(i + 1, path + [i], target - i, k)
            
        res=[]
        backtrack(1, [], n, k)
        return res
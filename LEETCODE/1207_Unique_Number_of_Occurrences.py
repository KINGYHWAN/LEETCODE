class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        l = {}

        for i in arr:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
        
        occur = set(l.values())

        return len(occur) == len(l.values())
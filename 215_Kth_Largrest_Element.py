import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        hp = nums[:k]
        heapq.heapify(hp)

        for x in nums[k:]:
            if x > hp[0]:
                heapq.heapreplace(hp, x)

        
        return hp[0]
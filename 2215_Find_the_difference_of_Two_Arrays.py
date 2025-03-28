class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        ele = nums1[:]

        for i in ele:
            if i in nums2:
                nums2.remove(i)
                nums1.remove(i)

        return [nums1, nums2]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
a = Solution()
result = a.findDifference(nums1, nums2)
print(result)
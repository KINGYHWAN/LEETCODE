class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution1
        # temp = set(nums)
        
        # hash = {}

        # for i in temp:
        #     cnt = nums.count(i)
        #     hash[i] = cnt

        # max_num = max(hash.values())
        # res = [k for k, v in hash.items() if v == max_num]

        # return res[0]



        # solution2
        count = 0
        majority = 0

        for i in range(len(nums)):
            if count == 0 and majority != nums[i]:
                majority = nums[i]
                count += 1
            elif majority == nums[i]:
                count += 1
            else:
                count -= 1
        
        return majority
            

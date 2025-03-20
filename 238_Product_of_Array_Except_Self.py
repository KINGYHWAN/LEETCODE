class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        res = []
        zero_num = nums.count(0)
        if zero_num == 1:
            for i in range(len(nums)):
                mul = mul * nums[i] if nums[i] != 0 else mul
        
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(mul)
                else:
                    res.append(0)
                    
        elif zero_num > 1:
            for i in range(len(nums)):
                res.append(0)
        else:
            for i in range(len(nums)):
                mul *= nums[i]
            
            for i in range(len(nums)):
                res.append(int(mul / nums[i]))
            
        return res
            
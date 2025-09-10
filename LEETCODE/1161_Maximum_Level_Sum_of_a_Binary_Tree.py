# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        
        앞에꺼 활용해서 level별로 sum 구하고 
        max_index + 1 하면 될 거 같은데..

        """

        if not root:
            return

        sum_result = []

        level = [root]

        while level:
            temp = []
            temp_sum = 0

            for i in level:
                temp_sum += i.val

                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                
            sum_result.append(temp_sum)
            level = temp.copy()
        
        max_num = max(sum_result)
        index = sum_result.index(max_num)

        return index + 1
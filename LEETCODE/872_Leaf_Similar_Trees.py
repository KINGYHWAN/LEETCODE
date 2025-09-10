# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_seq = []
        root2_seq = []

        if root1 is None and root2 is None:
            return True

        def dfs(tree, result):
            if tree.left:
                dfs(tree.left, result)
            if tree.right:
                dfs(tree.right, result)
            if tree.left is None and tree.right is None:
                result.append(tree.val)

            return result
        
        root1_seq = dfs(root1, root1_seq)
        root2_seq = dfs(root2, root2_seq)

        return root1_seq == root2_seq
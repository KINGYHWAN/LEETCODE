# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def f(root, p, q):

            if not root:
                return None
            
            if root.val == p.val:
                return root
            
            if root.val == q.val:
                return root
            
            left = f(root.left, p, q)
            right = f(root.right, p, q)

            if left and right:
                return root
            
            return left if left else right

        return f(root,p,q)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def checker(n1, n2):
            if not n1 or not n2:
                return n1 == n2
            if n1.left and n2.left and n1.left.val != n2.left.val or (n1.left and not n2.left) or (not n1.left and n2.left):
                n1.left, n1.right = n1.right, n1.left
            return n1.val == n2.val and checker(n1.left, n2.left) and checker(n1.right, n2.right)
        
        return checker(root1, root2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        idx = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            idx += 1
            if idx == k:
                return node.val
            root = node.right
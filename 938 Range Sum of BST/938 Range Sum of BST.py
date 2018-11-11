# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        BFS = [root]
        result = 0
        while BFS:
            root = BFS.pop(0)
            if root.left:
                BFS.append(root.left)
            if root.right:
                BFS.append(root.right)
            if root.val >= L and root.val <= R:
                result += root.val
        
        return result
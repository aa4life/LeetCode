# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        DFS = [root]
        while DFS:
            node = DFS.pop()
            if node:
                result.append(node.val)
                DFS.append(node.right)
                DFS.append(node.left)
                
        return result
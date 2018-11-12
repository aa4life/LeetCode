# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        DFS = [root]
        depth = 1
        maxdepth = 0
        passed = set()
        first = []
        second = []
        while DFS:
            passed.add(root)
            if root.left and root.left not in passed:
                depth += 1
                DFS.append(root.left)
                root = root.left
                continue
            if root.right and root.right not in passed:
                depth += 1
                DFS.append(root.right)
                root = root.right
                continue
            if depth == maxdepth:
                idx = 0
                while first[idx].val == DFS[idx].val:
                    idx += 1
                second = DFS[idx - 1]
            if depth > maxdepth:
                maxdepth = depth
                first = DFS.copy()
                second = []
            DFS.pop()
            depth -= 1
            if DFS:
                root = DFS[-1]

        if second:
            return second
        else:
            return first[-1]


        '''
        def finddeep(root):
            if not root: 
                return 0, None
            l = finddeep(root.left)
            r = finddeep(root.right)
            if l[0] > r[0]: 
                return l[0] + 1, l[1]
            elif l[0] < r[0]: 
                return r[0] + 1, r[1]
            else: 
                return l[0] + 1, root
        return finddeep(root)[1]
            '''
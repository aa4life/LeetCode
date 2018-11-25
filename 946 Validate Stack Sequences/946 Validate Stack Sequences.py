class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        nonpop = []
        for n in pushed:
            nonpop.append(n)
            while nonpop and popped[0] == nonpop[-1]:
                popped.pop(0)
                nonpop.pop()
        
        return not nonpop
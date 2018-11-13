class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        bound = -1
        for i in range(len(arr)):
            bound = max(bound, arr[i])
            if i == bound:
                bound = -1
                result += 1
        
        return result
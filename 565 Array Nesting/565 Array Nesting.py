class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runset = set()
        def findlen(i):
            if i in runset:
                return 0
            runset.add(i)
            return findlen(nums[i]) + 1
        
        result = 0
        for i in range(len(nums)):
            if i in runset:
                continue
            now = findlen(i)
            if now > result:
                result = now
        return result
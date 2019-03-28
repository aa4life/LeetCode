import collections

class Solution:
    def deleteAndEarn(self, nums):
        numdict = collections.Counter(nums)
        
        twobefore, prev, result = 0, 0, 0
        for n in range(10001):
            twobefore = prev
            prev = result
            result = max(twobefore + n * numdict[n], prev)
            
        return result
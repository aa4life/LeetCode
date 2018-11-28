import random

class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.val = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.val
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return random.sample(self.val, len(self.val))
    
    def shuffle2(self):
        ans = self.val[:]
        for i in range(len(ans)-1, 0, -1):
            j = random.randrange(0, i+1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
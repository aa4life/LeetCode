class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        t = abs(target)
        
        step = 0
        sumstep = 0
        while sumstep < t:
            step += 1
            sumstep += step
            
        if (sumstep - t) % 2 == 0:
            return step
        else:
            if step % 2 == 0:
                return step + 1
            if step % 2 == 1:
                return step + 2
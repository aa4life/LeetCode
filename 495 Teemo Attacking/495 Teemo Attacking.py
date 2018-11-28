class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """        
        starttime = 0
        endtime = 0
        result = 0
        for t in timeSeries:
            if endtime > t:
                endtime = t + duration
            else:
                if endtime > starttime:
                    result += (endtime - starttime)
                endtime = t + duration
                starttime = t
        
        result += (endtime - starttime)
        
        return result
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        alpha = []
        numeric = []
        cmpdict = {}
        for log in logs:
            first = log.split()[1]
            if first.isdigit():
                numeric.append(log)
            else:
                alpha.append(log)
                firstspace = log.index(' ')
                cmpdict[log] = log[firstspace+1:]
        
        alpha.sort(key= lambda x: cmpdict[x])
        return alpha + numeric
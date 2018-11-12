class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        
        rdict = {}
        for n in answers:
            if n not in rdict:
                rdict[n] = 1
            else:
                rdict[n] += 1
                
        result = 0
        for key in rdict:
            group = key + 1
            if rdict[key] % group == 0:
                result += group * (rdict[key]/ group)
            else:
                result += group * (rdict[key] // group) + group

        return int(result)
class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        if q == 0:
            return 0
        
        goup = True
        times = 0
        passlen = 0
        while True:
            passlen += q
            if passlen > p:
                passlen -= p
                goup = not goup
            times += 1
            if goup and times % 2 == 0 and passlen == p:
                return 2
            if goup and times % 2 == 1 and passlen == p:
                return 1
            if not goup and passlen == p:
                return 0
class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        
        tokensum = sum(tokens)
        point = 0
        while tokensum > P:
            if not tokens or P < tokens[0]:
                return point
            while tokens and P > tokens[0]:
                point += 1
                tokensum -= tokens[0]
                P -= tokens[0]
                tokens.pop(0)
            if len(tokens) == 1:
                return point
            point -= 1
            tokensum -= tokens[-1]
            P += tokens[-1]
            tokens.pop()
                
        return point + len(tokens)
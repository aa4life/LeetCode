class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        result = [0] * len(deck)
        nowadd = True
        while deck:
            for i in range(len(result)):
                if result[i] == 0:
                    if nowadd:
                        result[i] = deck.pop(0)
                    nowadd = not nowadd
        
        return result
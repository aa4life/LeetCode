class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        if H == len(piles):
            return max(piles)
        
        low = 1
        high = max(piles)

        while low < high:
            speed = (low + high) // 2
            time = 0
            for b in piles:
                time += (b + speed - 1) // speed
            
            if time > H:
                low = speed + 1
            else:
                high = speed
        
        return low
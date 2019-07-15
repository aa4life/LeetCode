class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        num = len(bits)
    
        index = 0
        while index < num:
            if index == num - 1: 
                return True
            if bits[index] == 1: 
                index += 2              
            else: 
                index += 1
        return False
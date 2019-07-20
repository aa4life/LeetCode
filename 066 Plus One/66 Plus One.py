class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits] 
        num = int("".join(s))
        num += 1
        res = [int(x) for x in str(num)] 
        return res
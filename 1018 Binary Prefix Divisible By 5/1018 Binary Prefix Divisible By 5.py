class Solution:
    def prefixesDivBy5(self, A):
        ans = []
        num = 0
        for a in A:
            num = (num << 1) + a
            if num % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
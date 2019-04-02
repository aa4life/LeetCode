class Solution:
    def lexicalOrder(self, n: int):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new //= 10
                new += 1
                while new % 10 == 0:
                    new //= 10
            ans.append(new)
            
        return ans
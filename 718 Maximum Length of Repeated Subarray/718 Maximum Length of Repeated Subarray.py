class Solution:
    def findLength(self, A, B):
        ans = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    ans[i + 1][j + 1] = ans[i][j] + 1
            
        return max(max(row) for row in ans)
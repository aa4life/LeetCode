class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        
        dp = [1] * 10
        result = 0
        for i in range(N - 1):
            num0 = dp[0]
            num1 = dp[1]
            num2 = dp[2]
            num3 = dp[3]
            num4 = dp[4]
            num6 = dp[6]
            num7 = dp[7]
            num8 = dp[8]
            num9 = dp[9]
            for j in range(10):
                if j == 5:
                    continue
                elif j == 0:
                    dp[j] = num4 + num6
                elif j == 1:
                    dp[j] = num6 + num8
                elif j == 2:
                    dp[j] = num7 + num9
                elif j == 3:
                    dp[j] = num4 + num8
                elif j == 4:
                    dp[j] = num0 + num3 + num9
                elif j == 6:
                    dp[j] = num0 + num1 + num7
                elif j == 7:
                    dp[j] = num2 + num6
                elif j == 8:
                    dp[j] = num1 + num3
                elif j == 9:
                    dp[j] = num2 + num4
                if i == N - 2:
                    result += dp[j]
        
        return result % (10 ** 9 + 7)
        
        '''
        counted = {}
        def getnextnumber(now, times, N):
            if N == 1:
                return 1
            if now == 0:
                if (4, N-1) in counted:
                    num1 = counted[(4, N-1)]
                else:
                    num1 = getnextnumber(4, times, N - 1)
                    counted[(4, N-1)] = num1
                if (6, N-1) in counted:
                    num2 = counted[(6, N-1)]
                else:
                    num2 = getnextnumber(6, times, N - 1)
                    counted[(6, N-1)] = num2
                count = times + num1 + num2
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 1:
                if (8, N-1) in counted:
                    num1 = counted[(8, N-1)]
                else:
                    num1 = getnextnumber(8, times, N - 1)
                    counted[(8, N-1)] = num1
                if (6, N-1) in counted:
                    num2 = counted[(6, N-1)]
                else:
                    num2 = getnextnumber(6, times, N - 1)
                    counted[(6, N-1)] = num2
                count = times + num1 + num2
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 2:
                if (7, N-1) in counted:
                    num1 = counted[(7, N-1)]
                else:
                    num1 = getnextnumber(7, times, N - 1)
                    counted[(7, N-1)] = num1
                if (9, N-1) in counted:
                    num2 = counted[(9, N-1)]
                else:
                    num2 = getnextnumber(9, times, N - 1)
                    counted[(9, N-1)] = num2
                count = times + num1 + num2
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 3:
                if (4, N-1) in counted:
                    num1 = counted[(4, N-1)]
                else:
                    num1 = getnextnumber(4, times, N - 1)
                    counted[(4, N-1)] = num1
                if (8, N-1) in counted:
                    num2 = counted[(8, N-1)]
                else:
                    num2 = getnextnumber(8, times, N - 1)
                    counted[(8, N-1)] = num2
                count = times + num1 + num2
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 4:
                if (3, N-1) in counted:
                    num1 = counted[(3, N-1)]
                else:
                    num1 = getnextnumber(3, times, N - 1)
                    counted[(3, N-1)] = num1
                if (9, N-1) in counted:
                    num2 = counted[(9, N-1)]
                else:
                    num2 = getnextnumber(9, times, N - 1)
                    counted[(9, N-1)] = num2
                if (0, N-1) in counted:
                    num3 = counted[(0, N-1)]
                else:
                    num3 = getnextnumber(0, times, N - 1)
                    counted[(0, N-1)] = num3
                count = times + num1 + num2 + num3
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 5:
                return 0
            elif now == 6:
                if (1, N-1) in counted:
                    num1 = counted[(1, N-1)]
                else:
                    num1 = getnextnumber(1, times, N - 1)
                    counted[(1, N-1)] = num1
                if (7, N-1) in counted:
                    num2 = counted[(7, N-1)]
                else:
                    num2 = getnextnumber(7, times, N - 1)
                    counted[(7, N-1)] = num2
                if (0, N-1) in counted:
                    num3 = counted[(0, N-1)]
                else:
                    num3 = getnextnumber(0, times, N - 1)
                    counted[(0, N-1)] = num3
                count = times + num1 + num2 + num3
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 7:
                if (2, N-1) in counted:
                    num1 = counted[(2, N-1)]
                else:
                    num1 = getnextnumber(2, times, N - 1)
                    counted[(2, N-1)] = num1
                if (6, N-1) in counted:
                    num2 = counted[(6, N-1)]
                else:
                    num2 = getnextnumber(6, times, N - 1)
                    counted[(6, N-1)] = num2
                count = times + num1 + num2
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 8:
                if (1, N-1) in counted:
                    num1 = counted[(1, N-1)]
                else:
                    num1 = getnextnumber(1, times, N - 1)
                    counted[(1, N-1)] = num1
                if (3, N-1) in counted:
                    num2 = counted[(3, N-1)]
                else:
                    num2 = getnextnumber(3, times, N - 1)
                    counted[(3, N-1)] = num2
                count = times + num1 + num2
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
            elif now == 9:
                if (2, N-1) in counted:
                    num1 = counted[(2, N-1)]
                else:
                    num1 = getnextnumber(2, times, N - 1)
                    counted[(2, N-1)] = num1
                if (4, N-1) in counted:
                    num2 = counted[(4, N-1)]
                else:
                    num2 = getnextnumber(4, times, N - 1)
                    counted[(4, N-1)] = num2
                count = times + num1 + num2
                if (now, N) not in counted:
                    counted[(now,N)] = count
                return count
        
        result = 0
        for i in range(10):
            result += getnextnumber(i, 0, N)
        return result % (10 ** 9 + 7)        
        '''
import numpy as np
from math import factorial

class Solution(object):
    def isInterleave(self, s1, s2, s3):

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        print(len(dp), len(dp[0]))
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1] 

       



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().isInterleave(s1, s2, s3))

# k = 3
# print(Solution().addDigitis(0))

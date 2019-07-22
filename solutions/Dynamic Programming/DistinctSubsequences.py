## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/distinct-subsequences/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Just like edit distance, but you can't skip a char from the target string.
## Time complexity:: O(MN)
## Space complexity:: O(M)
## Notes::

class Solution:
    def numDistinct(self, A, B):
        n = len(A)
        m = len(B)
        if n < m:
            return 0
        else:
            dp = [[1]+[0 for j in range(m)] for i in range(n+1)]
            
            for i in range(1, n+1):
                for j in range(1, m+1):
                    dp[i][j] = dp[i-1][j]
                    if A[i-1] == B[j-1]:
                        dp[i][j] += dp[i-1][j-1]
            
            return dp[-1][-1]

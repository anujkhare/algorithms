## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-iii/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: 
## Time complexity:: O()
## Space complexity:: O()
## Notes:: This is very tricky!
## Bookmarked:: Yes

class Solution:

    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        l = len(A)
        if l <= 1:
            return 0
        
        diffs = [A[ix] - A[ix-1] for ix in range(1, l)]
        dp = [0] * l
        for k in range(2):
            ndp = [0] * l
            for ix in range(1, l):
                for jx in range(ix):
                    s = dp[jx] + A[ix] - A[jx]
                    if s > ndp[ix]:
                        ndp[ix] = s
                ndp[ix] = max(ndp[ix], ndp[ix-1])
            dp = ndp

        return dp[-1]

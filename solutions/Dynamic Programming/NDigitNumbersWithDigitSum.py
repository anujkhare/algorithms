## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/n-digit-numbers-with-digit-sum-s-/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: f(N, s) = sum_i_0_9 f(N-1, s-i); find base condition and create a table
## Time complexity:: O(NS)
## Space complexity:: O(S)
## Notes::

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B == 0:
            return A == 0
        if A == 0:
            return 0
        dp = [0] * (B+1)  # n=0, s=0
        dp[0] = 1
        for n in range(A):
            cur = [0] * (B+1)
            for s in range(1, B+1):
                # if s == 0:
                #     continue
                for ix in range(10):
                    if s - ix < 0:
                        continue
                    cur[s] += dp[s-ix]
            dp = cur
        return dp[-1] % 1000000007

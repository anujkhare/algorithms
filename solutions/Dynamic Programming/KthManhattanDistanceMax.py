## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/kth-manhattan-distance-neighbourhood/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Its like doing A^n, just keep taking max with neighbours on the modified array.
## Time complexity:: O(MNK)
## Space complexity:: O(MN)
## Notes::

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        A, B = B, A
        m = len(A)
        if m == 0: return A
        n = len(A[0])
        if n == 0: return A
        
        if B == 0: return A
        
        dp = A
        for k in range(B):
            dp_k = [dp[]]
            for ix in range(m):
                dprow = []
                for jx in range(n):
                    maxval = dp[ix][jx]
                    if ix > 0:
                        maxval = max(maxval, dp[ix-1][jx])
                    if ix < m - 1:
                        maxval = max(maxval, dp[ix+1][jx])
                    if jx > 0:
                        maxval = max(maxval, dp[ix][jx-1])
                    if jx < n - 1:
                        maxval = max(maxval, dp[ix][jx + 1])
                    dprow.append(maxval)
                dp_k.append(dprow)
            dp = dp_k
        return dp

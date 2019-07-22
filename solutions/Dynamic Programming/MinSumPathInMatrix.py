## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/kingdom-war/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: f(i, j) = A[i, j] + min(f(i-1, j), f(i, j-1))
## Time complexity:: O()
## Space complexity:: O()
## Notes::
## Bookmarked:: No


class Solution:
    # @param A : list of list of integers
        # @return an integer
    def minPathSum(self, A):
        if len(A) == 0:
            return 0
        m, n = len(A), len(A[0])
        if n == 0:
            return 0
        
        prev = A[0]
        for ix in range(1, m):
            cur = [0] * n
            cur[0] = prev[0] + A[ix][0]
            for jx in range(1, n):
                cur[jx] = min(cur[jx-1], prev[jx]) + A[ix][jx]
            prev = cur

        return prev[-1]

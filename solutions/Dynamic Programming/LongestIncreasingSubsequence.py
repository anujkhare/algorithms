## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/longest-increasing-subsequence/
## Topic:: Dynamic Programming
## Sub-topic:: 2D string
## Difficulty:: Easy
## Approach::
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes:: There is a O(N logN) solution to this problem as well!

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if len(A) == 0:
            return 0
        
        maxlens = [1] * len(A)
        for ix in range(len(A)):
            for jx in range(ix):
                if A[ix] > A[jx]:
                    maxlens[ix] = max(maxlens[ix], maxlens[jx] + 1)
        return max(maxlens)
            

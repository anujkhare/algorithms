## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/jump-game-array/
## Topic:: Arrays
## Sub-topic:: Simple iteration
## Difficulty:: Easy
## Approach:: Just maintain the max reachable index and iterate, fail if you reach a greater index
## Time complexity:: O(n)
## Space complexity:: O(1)
## Notes::

class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        n = len(A)
        if n == 0: return 0
        maxreachable = 0
        for ix, a in enumerate(A):
            if ix > maxreachable:
                return 0
            maxreachable = max(maxreachable, ix + A[ix])
        return 1

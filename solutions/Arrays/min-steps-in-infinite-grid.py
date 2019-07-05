## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
## Topic:: Arrays
## Sub-topic:: Simple iteration
## Difficulty:: Easy
## Approach:
## Time complexity:: O(n)
## Space complexity:: O(1)
## Notes:


class Solution:
    # @param A :: list of integers
    # @param B :: list of integers
    # @return an integer
    def coverPoints(self, A, B):
        mindist = 0
        if len(A) == 0:
            return 0

        for ix in range(1, len(A)):
            dx = abs(A[ix] - A[ix - 1])
            dy = abs(B[ix] - B[ix - 1])
            sq = min(dx, dy)
            mindist += (dx + dy - sq)

        return mindist


## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/ways-to-color-a-3xn-board/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: f(N, s) = sum_i_0_9 f(N-1, s-i); find base condition and create a table
## Time complexity:: O(NS)
## Space complexity:: O(S)
## Notes::
## Bookmarked:: Yes


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0: return 0
        if A == 1: return 36
        
        dp2 = 12
        dp3 = 24
        for ix in range(1, A):
            ndp2 = dp2 * 7 + dp3 * 5
            ndp3 = dp2 * 10 + dp3 * 11
            dp2, dp3 = ndp2, ndp3
        return (dp2 + dp3) % 1000000007

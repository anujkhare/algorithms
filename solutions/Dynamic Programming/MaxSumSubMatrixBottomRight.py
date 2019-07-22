## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/kingdom-war/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Just check all the sub-matrices rooted at the bottom-right vertex
## Time complexity:: O(MN)
## Space complexity:: O(M)
## Notes::
## Bookmarked:: No

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        m = len(A)
        if m == 0: return 0
        n = len(A[0])
        if n == 0: return 0

        prev = [0] * (n + 1)
        maxarea = -float('inf')
        for ix in range(m-1, -1, -1):
            cur = [0] * (n+1)
            for jx in range(n-1, -1, -1):
                cur[jx] = cur[jx+1] + prev[jx] + A[ix][jx] - prev[jx + 1]
                maxarea = max(maxarea, cur[jx])
            prev = cur
        return maxarea


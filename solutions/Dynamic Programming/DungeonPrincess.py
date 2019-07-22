## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/dungeon-princess/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Work backwards and maintain the count
## Time complexity:: O(MN)
## Space complexity:: O(M)
## Notes::
## Bookmarked:: No


class Solution:
    # @param A : list of list of integers
        # @return an integer
    def calculateMinimumHP(self, A):
            m = len(A)
            if m == 0:
                return 0
            n = len(A[0])
            if n == 0:
                return 0
            
            # we'll go bottom to top, right to left
            prev = [float('inf')] * n
            prev[-1] = 1
            for ix in range(m-1, -1, -1):
                cur = [0] * n
                for jx in range(n-1, -1, -1):
                    below = prev[jx]
                    right = cur[jx + 1] if jx < n-1 else float('inf')
                    
                    cur[jx] = max(min(below, right) - A[ix][jx], 1)
                prev = cur
            return prev[0]

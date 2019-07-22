## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/min-sum-path-in-triangle/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Go from bottom to top and keep maintaining min path sum to that point
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes::
## Bookmarked:: No

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0][0]
    
        min_totals = A[-1]   # Last row as-is has the minimum values
        for level_num in range(len(A)-2, -1, -1):  # Go from the bottom to the top
            level = A[level_num]
            min_totals_new = []
    
            for ix in range(len(level)):
                min_totals_new.append(min(min_totals[ix], min_totals[ix+1]) + level[ix])
            min_totals = min_totals_new
    
        return min_totals[0]

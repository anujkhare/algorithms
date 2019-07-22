## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/min-jumps-array/
## Topic:: Greedy
## Sub-topic:: 1D 
## Difficulty:: Medium
## Approach:: At each step, jump to the position which will allow you to go the furthest.
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 

class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n == 0: return 0
        if n == 1: return 0
        cur = 0
        maxreachable = A[0]
        step = 1
        while True:
            if maxreachable >= n-1:
                return step

            new = 0
            while cur <= maxreachable and cur <= n-1:
                new = max(new, cur + A[cur])
                cur += 1
            
            if new == maxreachable:  # no more left to explore
                return -1
            maxreachable = new
            
            step += 1

        return -1

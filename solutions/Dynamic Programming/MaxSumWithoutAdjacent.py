## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/
## Topic:: Dynamic Programming
## Sub-topic:: 1D 
## Difficulty:: Easy
## Approach:: Again, simple, either pick the last one or don't. Add accordingly.
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 

from collections import deque

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        n = len(A[0])
        if n == 0:
            return 0
        arr = [max(a, b) for a, b in zip(A[0], A[1])]
        
        dp = deque([0, arr[0]])
        
        for ix in range(1, len(arr)):
            dp.append(max(dp[-2] + arr[ix], dp[-1]))
            dp.popleft()
        
        return dp[-1]

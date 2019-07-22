## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/stairs/
## Topic:: Dynamic Programming
## Sub-topic:: 1D
## Difficulty:: Easy
## Approach:: f(n) = f(n-1) + f(n-2)
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 

class Solution:
    # @param A : integer
            # @return an integer
    # @return an integer
    def climbStairs(self, A):
        if A == 0:
            return 0
    
        if A == 1:
            return 1
        if A == 2:
            return 2
    
        no_of_ways_1, no_of_ways_2 = 1, 2
        for ix in range(2, A):
            no_of_ways = no_of_ways_1 + no_of_ways_2
            no_of_ways_1 = no_of_ways_2
            no_of_ways_2 = no_of_ways
            
        return no_of_wa

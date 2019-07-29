## Website:: Self
## Link:: https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
## Topic:: Math
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Find the number of powers of 5
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 
## Bookmarked:: No

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        if A == 0:
            return 0
        div = 5
        count = 0
        while div <= A:
            count += A // div
            div *= 5
        return count

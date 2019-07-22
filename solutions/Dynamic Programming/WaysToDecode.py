## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/ways-to-decode/
## Topic:: Dynamic Programming
## Sub-topic:: 1D
## Difficulty:: Easy
## Approach:: f(n) = f(n-1) + f(n-2)
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: Two possibilities: either the last char is used independently to form a digit, or with the one before it. You need to check if these are valid, that's all.

class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if len(A) == 0:
            return 0
        
        ways_2, ways_1 = 1, 0
        if 1<= int(A[0]) <= 9:
            ways_1 = 1

        for ix in range(1, len(A)):
            ways = 0
            last = int(A[ix])
            if 1 <= last <= 9:
                ways += ways_1

            last2 = int(A[ix-1: ix+1])
            if 10 <= last2 <= 26:
                ways += ways_2

            ways_2, ways_1 = ways_1, ways
            
        return ways_1

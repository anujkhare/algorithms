## Website:: Self
## Link:: https://www.interviewbit.com/problems/greatest-common-divisor/
## Topic:: Math
## Sub-topic:: GCD
## Difficulty:: Easy
## Approach:: 
## Time complexity:: O(logN)
## Space complexity:: O(1)
## Notes:: The complexity for this is weird...
## Bookmarked:: Yes

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        A, B = min(A, B), max(A,  B)
        if A == 0: return B

        r = B % A
        if r == 0:
            return A
        return self.gcd(A, r)

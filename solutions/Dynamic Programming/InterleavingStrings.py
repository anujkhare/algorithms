## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/count-permutations-of-bst/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: notice that the length in the target string depends on the lengths of the substrings chosen in the two other strings.
## Time complexity:: O(MN)
## Space complexity:: O(MN)
## Notes:: 
## Bookmarked:: No

class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        la, lb, lc = len(A), len(B), len(C)
        if la + lb != lc:
            return int(False)
        if la == 0:
            return int(B == C)
        if lb == 0:
            return int(A == C)
 
        a, b, c = A[-1], B[-1], C[-1]
        
        possible = False
        if c == a:
            possible = possible or self.isInterleave(A[:-1], B, C[:-1])
        if c == b:
            possible = possible or self.isInterleave(A, B[:-1], C[:-1])
        return int(possible)

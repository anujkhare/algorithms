## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/intersecting-chords-in-a-circle/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Iterate over all possible first chords such that you split the problem into 2 subproblems; f(P) = Sum f(P-i) * f(i-2), i = 1...P, P = number of points
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes::

MOD = int(1e9 + 7)


class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        if A <= 1:
            return 1

        F = [0] * (A+1)
        F[0] = F[1] = 1
        for ix in range(2, A+1):
            for jx in range(ix):
                F[ix] += (F[jx] * F[ix - jx - 1]) % MOD
            F[ix] = F[ix] % MOD
                
        return  int(F[A] % MOD)

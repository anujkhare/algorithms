## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/edit-distance/
## Topic:: Dynamic Programming
## Sub-topic:: 2D string
## Difficulty:: Easy
## Approach:: f(m, n) = f(m-1, n-1) if match, else min(f(m-1, n-1), f(m, n-1), f(m-1, n))
## Time complexity:: O(MN)
## Space complexity:: O(min(M, N))
## Notes:: 

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        if len(A) >= len(B):
            longer, shorter = A, B
        else:
            longer, shorter = B, A
        ll = len(longer)
        ls = len(shorter)
        if ls == 0:
            return la

        prev = list(range(ls + 1))
        for ix in range(1, ll + 1):
            cur = [0] * (ls + 1)
            cur[0] = ix
            for jx in range(1, ls + 1):
                if longer[ix - 1] == shorter[jx - 1]:
                    cur[jx] = prev[jx - 1]
                    continue
                cur[jx] = 1 + min(cur[jx - 1], prev[jx - 1], prev[jx])
            prev = cur
        return cur[-1]

## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/anti-diagonals/
## Topic:: Arrays
## Sub-topic:: Simple iteration
## Difficulty:: Easy
## Approach:: kth anti-diagonal is ix + jx = k, kth diagonal ix - jx = k
## Time complexity:: O(n*n)
## Space complexity:: O(n)
## Notes:


class Solution:
    # @param A :: list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        if n == 0:
            return []
        if n != len(A[0]):
            raise ValueError

        antis = [[] for _ in range(2 * n - 1)]
        for ix in range(n):
            for jx in range(n):
                s = ix + jx
                antis[s].append(A[ix][jx])
        return antis
## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/add-one-to-number/
## Topic:: Arrays
## Sub-topic:: Simple iteration
## Difficulty:: Easy
## Approach::
## Time complexity:: O(n)
## Space complexity:: O(1)
## Notes::


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) == 0:
            return [1]

        while len(A) > 0 and A[0] == 0:
            A = A[1:]

        r = 1
        for ix in range(len(A) - 1, -1, -1):
            d = A[ix]
            s = d + r
            A[ix] = s % 10
            r = s // 10
        if r > 0:
            A.insert(0, r)
        return A

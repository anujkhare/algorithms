## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/repeat-and-missing-number-array/
## Topic:: Arrays
## Sub-topic:: Simple iteration
## Difficulty:: Easy
## Approach:: Maintain a hash map within the array by setting seen positions as negative
## Notes:

class Solution:
    # @param A :: tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        if len(A) <= 1:
            return []
        A = list(A)
        dup = None
        for ix, a in enumerate(A):
            pos = abs(a) - 1
            if A[pos] < 0:
                dup = pos + 1
                break
            A[pos] *= -1
        if dup is None:
            raise ValueError
        A = [abs(a) for a in A]
        missing = ((len(A) * (len(A)+1)) / 2) - (sum(A) - dup)
        return [dup, missing]

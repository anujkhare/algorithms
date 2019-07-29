## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
## Topic:: Hashing
## Sub-topic:: Prefix sum
## Difficulty:: Medium
## Approach:: Calculate the cumsum and hash the earliest location where you saw the cumsum; if the cumsum is 5 and you've seen a 5 before, that subsequence is 0 sum!
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes::

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        lastsum = {0: -1}
        cursum = 0
        maxlen, inds = 0, None
    
        for ix, a in enumerate(A):
            cursum += a
            if cursum in lastsum:
                jx = lastsum[cursum]
                seqlen = ix - jx
                if maxlen < seqlen:
                    maxlen = seqlen
                    inds = (jx + 1, ix)
                continue
            lastsum[cursum] = ix

        if inds is None:
            return []
        return A[inds[0]: inds[1] + 1]

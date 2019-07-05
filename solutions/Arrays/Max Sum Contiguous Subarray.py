## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
## Topic:: Arrays
## Sub-topic:: Simple iteration
## Difficulty:: Easy
## Approach:: Whenever the sum becomes negative, just start afresh
## Time complexity:: O(n)
## Space complexity:: O(1)
## Notes:

class Solution:
    # @param A :: tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        l = len(A)
        if l == 0:
            return 0
        maxsum = 0
        cursum = 0
        for a in A:
            cursum += a
            if cursum < 0:
                cursum = 0
            maxsum = max(maxsum, cursum)
        return maxsum


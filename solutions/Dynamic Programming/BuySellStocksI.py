## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Take the diffs, then do maximum sum subarray
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes::
## Bookmarked:: No

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)
        if n < 2:
            return 0
        diffs = [A[i] - A[i-1] for i in range(1, n)]
        maxsum = 0
        cursum = 0
        
        for d in diffs:
            cursum += d
            maxsum = max(maxsum, cursum)
            cursum = max(cursum, 0)
        
        return maxsum

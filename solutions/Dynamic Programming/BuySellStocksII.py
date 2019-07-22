## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-ii/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: This is stupid, you would basically buy and sell whenever you can make a profit, each day.
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes::
## Bookmarked:: No

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)
        if n == 0:
            return 0
        
        diffs = [A[ix] - A[ix-1] for ix in range(1, n)]
        total = sum(filter(lambda x: x > 0, diffs))
        return total

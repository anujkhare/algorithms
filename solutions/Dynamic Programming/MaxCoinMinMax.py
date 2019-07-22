## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/coins-in-a-line/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: It's a classic min-max problem!
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes:: Looking at it from the total sum perspective makes it so much easier!
## Bookmarked:: Yes

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        n = len(A)
        if n == 0: return 0
        if n == 1: return A[0]
        
        cursum = 0
        cumsums = []
        for ix in range(n):
            cursum += A[ix]
            cumsums.append(cursum)
        
        dp = A
        for l in range(2, n+1):
            ndp = []  # the new dp array for this length
            for start in range(n - l + 1):
                end = start + l - 1
                totalsum = cumsums[end] - cumsums[start] + A[start]
                maxsum = totalsum - min(dp[start], dp[start+1])
                # print(maxsum)
                ndp.append(maxsum)
            # print()
            # print()
                
            dp = ndp
        return dp[-1]
                
                

## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/unique-binary-search-trees-ii/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: f(N, s) = sum_i_N f(i) * f(N-1-i), s-i)
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes::
## Bookmarked:: No

class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        dp = [1, 1]  # 0, 1
        for n in range(2, A+1):
            count = 0
            for ix in range(n):
                count += (dp[ix] * dp[n - ix -1])
            dp.append(count)
        return dp[-1]

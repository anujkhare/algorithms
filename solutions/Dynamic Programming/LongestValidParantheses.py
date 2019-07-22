## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/longest-valid-parentheses/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Store DP of the length of longest val paran ending at i; if the ith char ')', create cases
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: Alternatively, use a stack to find the length of the valid paran sub-sequences, be sure to accout for cases like "(()) (())" by storing prevmax
## Bookmarked:: Yes

class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        n = len(A)
        if n == 0: return 0
        maxlen = 0
        stack = []
        dp = {}
        for ix, a in enumerate(A):
            if a == '(':
                stack.append(ix)
                continue
            if len(stack) == 0:
                continue
            top = stack.pop()
            prevmax = dp.get(top-1, 0)
            curmax = ix - top + 1 + prevmax
            dp[ix] = curmax
            maxlen = max(maxlen, curmax)
        return maxlen

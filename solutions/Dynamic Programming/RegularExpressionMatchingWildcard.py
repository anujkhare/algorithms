## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/regular-expression-match/
## Topic:: Dynamic Programming
## Sub-topic:: 2D
## Difficulty Just create a 2D table and write rules similar to edit distance
## Approach:: 
## Time complexity:: O(MN)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: No


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        string = A
        pattern = B
        
        new_pattern = []
        prev = None
        for p in pattern:
            if p == '*' and prev == p:
                continue
            prev = p
            new_pattern.append(prev)
        pattern = ''.join(new_pattern)
        
        l = len(string)
        dp = [[0] * (l + 1) for _ in range(len(pattern) + 1)]  # 0 based
        dp[0][0] = 1  # both string and pattern emtpy
        for ixp, p in enumerate(pattern):
            if p == '*':
                dp[ixp+1][0] = dp[ixp][0]

            for ix, s in enumerate(string):
                if p == '*':
                    dp[ixp + 1][ix + 1] = int(dp[ixp][ix] or dp[ixp + 1][ix] or dp[ixp][ix + 1])
                    continue
                
                # pattern is a single char wildcard
                if p == '?':
                    dp[ixp + 1][ix + 1] = dp[ixp][ix]
                    continue
                
                # both chars, not equal
                if p != s:
                    continue

                # both chars, equal
                dp[ixp + 1][ix + 1] = dp[ixp][ix]
        
        return dp[-1][-1]

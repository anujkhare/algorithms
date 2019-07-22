## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/regular-expression-ii/
## Topic:: Dynamic Programming
## Sub-topic:: 2D
## Difficulty:: Medium
## Approach:: This is tricky since you can match 0 characters as well..
## Time complexity:: O(MN)
## Space complexity:: O(M)
## Notes:: Here, the * is like a modifier, so you can just pre-process the input to make it into a format that is easy to use.
## Bookmarked:: No


class Solution:
    def _match(self, s, p):
        return s == p or p == '.'

    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        string = A.strip()
        pattern = B
        
        l = len(string)

        # Convert into alphabets, single/multiple
        new_pattern = [[None, 0]]
        for p in pattern:
            if p == '*':
                new_pattern[-1][1] = 1
                continue
            new_pattern.append([p, 0])

        # print(new_pattern)

        # match prefixes!
        # print(l, string)
        dp = [0] * (l + 1)
        dp[0] = 1
        for p, multiple in new_pattern[1:]:
            # print('foo')
            ndp = [0] * (l + 1)
            if multiple:  # 0 matches possible with this character
                ndp[0] = dp[0]
            
            for ix, s in enumerate(string):
                match = self._match(s, p)

                # last char can be multiple matched
                if multiple:
                    if not match:
                        ndp[ix + 1] = dp[ix + 1]
                    else:
                        ndp[ix + 1] = int(dp[ix + 1] or dp[ix] or ndp[ix])
                    continue
                
                # Single matching char in pattern
                if match:
                    ndp[ix + 1] = dp[ix]
                else:
                    ndp[ix + 1] = 0
            
            # print(ndp)
            dp = ndp
        
        # print(dp)
        return dp[-1]

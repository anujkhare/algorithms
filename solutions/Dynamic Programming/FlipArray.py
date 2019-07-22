## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/flip-array/
## Topic:: Dynamic Programming
## Sub-topic:: Knapsack
## Difficulty:: Hard
## Approach:: for each sum b/w 0...sum(arr)//2, compute the min number of elements that will give that sum; find the one that is closest to and less than N//2
## Time complexity:: O(NS)
## Space complexity:: O(S)
## Notes:: This is similar to the knapsack problem I think
## Bookmarked:: Yes

import math


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return 0
        A = sorted(A)
        S = sum(A)
        dp = [float('inf')] * (S + 1)
        dp[0] = 0  # 0sum, no numbers
        
        for ix, a in enumerate(A):
            ndp = [float('inf')] * (S + 1)
            ndp[0] = 0
            for s in range(S+1):
                ndp[s] = min(ndp[s], dp[s])
                if a > s:
                    continue
                # print(a, s, ndp[s], dp[s-a], dp[s])
                ndp[s] = min(ndp[s], dp[s-a] + 1)
                # print(ndp[s])
            # print(a, ndp)
            dp = ndp
            # print(dp[:5])
    
        mindiff = float('inf')
        count = float('inf')
        
        # print(A)
        # print(S)
        # print(dp)
        # for s, d in enumerate(dp[150:]):
        #     print(s+150, d)
        for s in range(S+1):
            if dp[s] == float('inf'):
                continue
            diff = S/2. - s
            if diff < 0:
                continue
            elif diff < mindiff:
                mindiff = diff
                count = dp[s]
        return count

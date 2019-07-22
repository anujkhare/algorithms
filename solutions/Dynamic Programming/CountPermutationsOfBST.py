## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/count-permutations-of-bst/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: 
## Time complexity:: O()
## Space complexity:: O()
## Notes:: 
## Bookmarked:: Yes


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def get_ncr(self, n):
        ncr = [[1], [1, 1]]
        for ix in range(2, n+1):
            row = [1]
            for jx in range(1, ix):
                row.append(ncr[ix-1][jx] + ncr[ix-1][jx-1])
            row.append(1)  # nCn
            ncr.append(row)
        return ncr
        
    def cntPermBST(self, A, B):
        if A == 0:
            return 0
        if B == 0:
            return A == 1
        
        ncr = self.get_ncr(51)
        dp = [[0] * (A+1) for _ in range(A)]  # height = 0...B
        dp[0][0] = 1  # n=1, h=0

        for n in range(2, A+1):
            for root in range(n):
                nleft = root
                nright = n - root - 1
                
                # print('n', n, 'left', nleft, 'right', nright)
                if nleft == 0:
                    for hright in range(nright):
                        dp[n-1][hright+1] += dp[nright-1][hright]
                    continue
                if nright == 0:
                    for hleft in range(nleft):
                        dp[n-1][hleft+1] += dp[nleft-1][hleft]
                    continue
                for hleft in range(nleft):
                    for hright in range(nright):
                        w1, w2 = dp[nleft-1][hleft], dp[nright-1][hright]
                        height = 1 + max(hleft, hright)
                        combs = ncr[nleft+nright][nleft]
                        ways = w1 * w2 * combs
                        # print(hleft, hright, w1, w2, height, combs, ways)
                        dp[n-1][height] += ways
        # print(ncr)
        # print(dp)
        return dp[A-1][B] % int(1e9 + 7)

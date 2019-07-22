## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/longest-arithmetic-progression/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Memoize the longest sequence up to i for each possible difference. Alternatively, same as memoizing for the ending pair (i, j)
## Time complexity:: O(N^2)
## Space complexity:: O(N^2)
## Notes::


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        l = len(A)
        if l == 0: return 0
        if l == 1: return 1
        
        maxlen = 0
        dp = [{}]  # mapping: d -> max_ap_len upto that index with d=d
        for ix in range(1, l):
            mem = {}
            for jx in range(ix):
                d = A[ix] - A[jx]   
                seqlen = 1 + dp[jx].get(d, 1)
                mem[d] = max(mem.get(d, 0), seqlen)
                
                maxlen = max(maxlen, seqlen)
            dp.append(mem)
        
        return maxlen
        

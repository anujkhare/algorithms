## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/length-of-longest-subsequence/
## Topic:: Dynamic Programming
## Sub-topic:: 1D
## Difficulty:: Easy
## Approach:: Find the longest increasing subsequence from the start and from the end (of the reverse); iterate and find the maximum sum - 1.
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes:: 


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        if len(A) == 0:
            return 0
        
        def find_longest_inc(arr):
            inc_len = [1] * len(arr)
            for ix in range(1, len(arr)):
                for jx in range(ix):
                    if arr[jx] < arr[ix]:
                        inc_len[ix] = max(inc_len[ix], inc_len[jx] + 1)
            return inc_len
        
        left_inc_len = find_longest_inc(A)
        right_inc_len = find_longest_inc(A[::-1])[::-1]

        maxval = 0
        for ix in range(len(A)):
            maxval = max(maxval, left_inc_len[ix]+right_inc_len[ix])
        return maxval-1


## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/longest-substring-without-repeat/
## Topic:: Hashing
## Sub-topic:: Search, two pointers
## Difficulty:: Easy
## Approach:: Just store the last seen position for each character; if a new one comes, the curstart has to be at least as large as that;
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: The 2 pointers based approach will go iteratively moving p_left till we have unique characters between p_left and p_right

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        lastpos = {}
        curstart, maxlen = -1, 0
        for ix, a in enumerate(A):
            curstart = max(lastpos.get(a, -1), curstart)
            maxlen = max(maxlen, ix - curstart)
            lastpos[a] = ix
        return maxlen

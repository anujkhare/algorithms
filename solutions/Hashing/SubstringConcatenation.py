## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/substring-concatenation/
## Topic:: Hashing
## Sub-topic:: Key formation
## Difficulty:: Easy
## Approach:: Just split the words from each substring in the string and compare
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if len(B) == 0:
            return []
        
        l = len(A)
        target = ''.join(sorted(B))
        l_target, l_word = len(target), len(B[0])
    
        inds = []
        for ix in range(l - l_target + 1):
            s = A[ix: ix + l_target]
            words = [s[jx * l_word: (jx + 1) * l_word] for jx in range(len(B))]
            s_sorted = ''.join(sorted(words))
            if s_sorted == target:
                inds.append(ix)

        return inds

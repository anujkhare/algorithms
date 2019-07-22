## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/word-break-ii/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Do this recursively, check if each word exists in the dictionary or not
## Time complexity:: O()
## Space complexity:: O()
## Notes::
## Bookmarked:: No

import copy


class Solution:
    def helper(self, string, words):
        l = len(string)
        if l == 0: return [[]]
        if string in self.memory:
            return self.memory[string]
        
        all_lists = []
        for ix in range(l):
            prefix = string[:ix+1]
            if prefix not in words:
                continue
            lists = self.helper(string[ix+1:], words)
            for l in lists:
                lc = copy.deepcopy(l)
                lc.append(prefix)
                all_lists.append(lc)
        self.memory[string] = all_lists
        return all_lists
        
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        self.memory = {}
        all_lists = self.helper(A, set(B))
        all_lists = [' '.join(l[::-1]) for l in all_lists]
        return all_lists

## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/simplify-directory-path/
## Topic:: Stacks
## Sub-topic:: Simple
## Difficulty:: Easy
## Approach:: 
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        l = ['']
        for p in A.split('/'):
            if p == '':
                continue
            if p == '.':
                continue
            if p == '..':
                if len(l) == 1:
                    continue
                _ = l.pop()
                continue
            l.append(p)
        return '/'.join(l)

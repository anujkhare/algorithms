## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/redundant-braces/
## Topic:: Stacks
## Sub-topic:: Simple
## Difficulty:: Medium
## Approach:: 
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        l = len(A)
        if l == 0: return 0
        st = []
        lastpopped = None
        for ix, a in enumerate(A):
            if a != ')':
                st.append(a)
                continue
            # print(st)
            l_exp = 0
            while len(st) > 0 and st[-1] != '(':
                lastpopped = st.pop()
                l_exp += 1
            # print(st)
            if lastpopped == '(' or l_exp < 2:
                return 1
            lastpopped = st.pop()
        return 0

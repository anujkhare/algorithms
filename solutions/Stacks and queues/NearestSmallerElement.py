## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/nearest-smaller-element/
## Topic:: Stacks
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Maintain stack; while new element is smaller than or equal to top, pop; then insert
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        st = []
        g = []
        
        for a in A:
            while len(st) > 0 and st[-1] >= a:
                st.pop()
            if len(st) == 0:
                g.append(-1)
            else:
                g.append(st[-1])
            st.append(a)
 
        return g

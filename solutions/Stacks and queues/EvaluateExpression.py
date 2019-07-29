## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/evaluate-expression/
## Topic:: Stacks
## Sub-topic:: Reverse Polish Notation
## Difficulty:: Easy
## Approach:: 
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        st = []
        for a in A:
            if a not in ['+', '-', '*', '/']:
                st.append(a)
                continue
            o1, o2 = int(st.pop()), int(st.pop())
            if a == '+':
                st.append(o1 + o2)
            elif a == '-':
                st.append(o1 - o2)
            elif a == '*':
                st.append(o1 * o2)
            else:
                st.append(o1 // o2)
        return st[-1]

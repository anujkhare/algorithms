## Website:: Self
## Link:: https://www.interviewbit.com/problems/excel-column-number/
## Topic:: Math
## Sub-topic:: Base conversion
## Difficulty:: Easy
## Approach:: 
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:
## Bookmarked:: No

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
        return sum(T[ch] * 26**i for i, ch in enumerate(A[::-1]))
      

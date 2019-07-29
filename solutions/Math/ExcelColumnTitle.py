## Website:: Self
## Link:: https://www.interviewbit.com/problems/excel-column-title/
## Topic:: Math
## Sub-topic:: Base conversion
## Difficulty:: Easy
## Approach:: Divide by 26, take remainder; be careful that there is no 0 here, so you need to account for that
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:
## Bookmarked:: No

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        if A == 0:
            return ''
        num = []
        while A:
            r = A % 26
            if r == 0: r = 26
            num.append(chr(r + ord('A') - 1))
            A -= r
            A //= 26
        return ''.join(num[::-1])

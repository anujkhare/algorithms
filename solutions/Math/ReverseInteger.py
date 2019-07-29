## Website:: Self
## Link:: https://www.interviewbit.com/problems/reverse-integer/
## Topic:: Math
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Be careful with the signs!
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:
## Bookmarked:: No

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A == 0:
            return A
        sign = -1 if A < 0 else 1
        A = abs(A)
        digits = []
        while A:
            digits.append(A%10)
            A //= 10
        num = int(''.join([str(d) for d in digits]))
        if (sign > 0 and num > 2**16) or (sign < 0 and num >= 2 ** 16):
            return 0
        num *= sign
        return num

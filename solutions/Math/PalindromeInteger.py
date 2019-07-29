## Website:: Self
## Link:: https://www.interviewbit.com/problems/excel-column-title/
## Topic:: Math
## Sub-topic::
## Difficulty:: Easy
## Approach:: Subtract the last digit * 10^(number of digits)
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:
## Bookmarked:: No

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A == 0:
            return 1
        if A < 0:
            return 0
        ndigits = 0
        n = A
        while n > 0:
            ndigits += 1
            n //= 10

        # print(ndigits)
        n = A
        while True:
            if ndigits <= 1:
                return 1

            lastdigit = n % 10
            multiplier = lastdigit * (10 ** (ndigits-1))
            # print(lastdigit, n, multiplier)
            n -= multiplier
            
            if n < 0 or n > multiplier:
                return 0
            n //= 10
            ndigits -= 2
        
        return 1

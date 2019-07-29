## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/colorful-number/
## Topic:: Hashing
## Sub-topic:: Simple
## Difficulty:: Easy
## Approach:: Just store the product of each substring
## Time complexity:: O(N^3)
## Space complexity:: O(N^2)
## Notes::

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        digits = []
        num = A
        while num:
            digits.append(num % 10)
            num //= 10
            
        prods = set()
        for ix in range(len(digits)):
            for jx in range(ix, len(digits)):
                prod = 1
                for d in digits[ix: jx+1]:
                    prod *= d
                print(prod, prods, ix, jx)
                if prod in prods:
                    return 0
                prods.add(prod)
        return 1

## Website:: Self
## Link:: https://www.interviewbit.com/problems/power-of-two-integers/
## Topic:: Math
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: Find all prime numbers till A, check if two of them sum to A
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:
## Bookmarked:: Yes

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A == 0:
            return []
        primes = [1] * (A+1)
        for ix in range(2, A):
            if primes[ix] == 0: continue
            p = 2 * ix
            while p < A:
                primes[p] = 0
                p += ix
        
        for p in range(2, A//2 + 1):
            q = A - p
            if primes[p] and primes[q]:
                return [p, q]
        return None



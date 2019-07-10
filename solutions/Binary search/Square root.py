## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/add-one-to-number/
## Topic:: Binary Search
## Sub-topic:: Array
## Difficulty:: Easy
## Approach:: Just bsearch on the square of the mid value, consider corner cases
## Time complexity:: O(log(N))
## Space complexity:: O(1)
## Notes:: 

class Solution:
    def sqrt(self, A):
        if A < 0:
            return None
        if A <= 1:
            return A
        
        lo, hi = 2, A
        while lo < hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == A:
                return mid
            if sq < A:
                lo  = mid + 1
            else:
                hi = mid
        return lo - 1


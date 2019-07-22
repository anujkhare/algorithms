## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/max-product-subarray/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Maintain a positive and a negative prod; update based on the sign of a_i
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 
## Bookmarked:: No

class Solution:
    def maxProduct(self, A):
        if len(A) == 0:
            return None
        if len(A) == 1:
            return A[0]
        negprod, posprod = 0, 0
        maxprod = -float('inf')
        for ix, a in enumerate(A):
            if a == 0:
                negprod, posprod = 0, 0
            elif a > 0:
                posprod_ = posprod * a if posprod != 0 else a  # start afresh if 0!
                negprod_ = negprod * a
                posprod, negprod = posprod_, negprod_
            elif a < 0:
                posprod_ = negprod * a
                negprod_ = posprod * a if posprod != 0 else a
                posprod, negprod = posprod_, negprod_

            if maxprod < max(posprod, negprod):
                maxprod = max(posprod, negprod)
                # print(ix, a, posprod, negprod)
        return maxprod
            

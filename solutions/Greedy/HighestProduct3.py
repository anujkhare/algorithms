## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/highest-product/
## Topic:: Greedy
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Either the 3 largest numbers, or the 2 smallest (negative) and the largest.
## Time complexity:: O(NlogN)
## Space complexity:: O(1)
## Notes:: 
## Bookmarked:: No

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort(reverse = True)
        return max(A[0]*A[1]*A[2] , A[0]*A[-1]*A[-2])

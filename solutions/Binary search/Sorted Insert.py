## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/sorted-insert-position/
## Topic:: Binary Search
## Sub-topic:: Array
## Difficulty:: Easy
## Approach:: just return any of bisect left or right
## Time complexity:: O(log(N))
## Space complexity:: O(1)
## Notes::

class Solution:
    def searchInsert(self, A, B):
        l = len(A)
        lo, hi = 0, l
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] < B:
                lo = mid + 1
            else:
                hi = mid
        return lo


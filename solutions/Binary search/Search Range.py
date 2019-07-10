## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/matrix-search/
## Topic:: Binary Search
## Sub-topic:: Array
## Difficulty:: Easy
## Approach:: bisect left and right, return the range
## Time complexity:: O(log(N))
## Space complexity:: O(1)
## Notes::
import bisect

class Solution:
    def bisect_left(self, arr, target):
        if len(arr) == 0:
            return 0
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
    def bisect_right(self, arr, target):
        if len(arr) == 0:
            return 0
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
    def searchRange(self, A, B):
        ll = len(A)
        if ll == 0:
            return [-1, -1]
        
        l = self.bisect_left(A, B)
        r = self.bisect_right(A, B)
        # print(l, r)
        # print('foo')
        if l >= ll or A[l] != B:
            return [-1, -1]
        return [l, r-1]

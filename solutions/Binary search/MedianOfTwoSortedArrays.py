## Website:: Leetfree, Interviewbit
## Link:: https://www.interviewbit.com/problems/median-of-array/
## Topic:: Binary search
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: 
## Time complexity:: O(log(M+N))
## Space complexity:: O(1)
## Notes:: 
## Bookmarked:: Yes

import bisect


class Solution:
    def find_median(self, arr1, arr2, target):
        lo, hi = 0, len(arr1)
        while lo < hi:
            mid = (lo + hi) // 2
            pl = bisect.bisect_left(arr2, arr1[mid])
            pr = bisect.bisect_right(arr2, arr1[mid])
            
            minn, maxn = mid + pl, mid + pr
            if minn <= target <= maxn:
                return arr1[mid]
            elif maxn < target:
                lo = mid + 1
            else:
                hi = mid
    
    def findMedianSortedArrays(self, A, B):
        la, lb = len(A), len(B)
        l = la + lb
        
        median1, median2 = 0, 0

        target = l // 2

        median1 = self.find_median(A, B, target)
        if median1 is None: median1 = self.find_median(B, A, target)

        if l % 2 == 1:
            return int(median1)
        
        median2 = self.find_median(A, B, target - 1)
        if median2 is None: median2 = self.find_median(B, A, target - 1)
        ans = (median1 + median2) / 2.
        # print('tw', median1, median2, ans)
        return ans

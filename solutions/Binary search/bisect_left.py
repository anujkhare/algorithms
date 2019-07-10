## Website:: Self
## Link:: 
## Topic:: Binary Search
## Sub-topic:: Array
## Difficulty:: Easy
## Approach:: ...
## Time complexity:: O(log(N))
## Space complexity:: O(1)
## Notes:: bisect_left returns the left-most position which is greater than or equal to target

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
        

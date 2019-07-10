## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/add-one-to-number/
## Topic:: Binary Search
## Sub-topic:: Array
## Difficulty:: Medium
## Approach:: Divide into multiple cases based on which part of the segment you are seeing, update left/right.
## Time complexity:: O(log(N))
## Space complexity:: O(1)
## Notes:: This one just requires you to work out all the cases on a paper


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        
        lo, hi = 0, l
        while lo < hi:
            mid = (lo + hi) // 2
            a, b, c = nums[lo], nums[mid], nums[hi-1]
            
            if target == b:
                return mid

            # case 1:
            if a <= b <= c:
                if target > b:
                    lo = mid + 1
                else:
                    hi = mid
            elif b >= a and b >= c:
                if target > b:
                    lo = mid + 1
                # these depend on the extreme values as well
                elif target <= c:
                    lo = mid + 1
                else:
                    hi = mid
            elif b <= a and b <= c:
                if target < b:
                    hi = mid
                # these depend on the extreme values as well
                elif target <= c:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                raise
        return -1

## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/largest-area-of-rectangle-with-permutations/
## Topic:: Dynamic Programming
## Sub-topic:: 2D 
## Difficulty:: Medium
## Approach:: For each row, get the count of contiguous ones in each column; sort them; find the largest contiguous area
## Time complexity:: O(MN)
## Space complexity:: O(MN)
## Notes:: Intuition: start with 1 row; The intuition from counting sort should come from the fact that you know the range of the values (0...M).
## Bookmarked:: Yes


class Solution:
    def find_c_ones_in_col(self, arr):
        m, n = len(arr), len(arr[0])
        result = [arr[-1]]

        for ix in range(m-2, -1, -1):
            row = arr[ix]
            ones = []
            for jx in range(n):
                if arr[ix][jx] == 0:
                    ones.append(0)
                else:
                    ones.append(1 + result[-1][jx])
            result.append(ones)
    
        return result[::-1]

    def largest_rect_from_counts(self, counts):
        n = len(counts)
        maxarea, curwidth = 0, 0
        for jx in range(n - 1, 0, -1): # we don't care about height 0
            h, w = jx, counts[jx]
            if w == 0:      # there is no rect of this height
                continue
            curwidth += w
            maxarea = max(maxarea, curwidth * h)
        return maxarea
    
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        m, n = len(A), len(A[0])
        
        # find the number of contiguous 1's downwards from each i, j
        contiguous_ones = self.find_c_ones_in_col(A)
        # print(contiguous_ones)
        
        maxarea = 0
        for ix in range(m):
            # count the heights of each col
            height_counts = [0] * (m + 1)
            for jx in range(n):
                height_counts[contiguous_ones[ix][jx]] += 1
            
            # find the largest rectangle using the heights
            largest_rect_area = self.largest_rect_from_counts(height_counts)
            maxarea = max(maxarea, largest_rect_area)
        
        return maxarea

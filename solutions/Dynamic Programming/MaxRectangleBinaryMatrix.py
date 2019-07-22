## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: Count column wise prefix sums; fix a pair of rows; find the max contiguous ones in between the two rows and calculate area
## Time complexity:: O(N^3) | O(N^2)
## Space complexity:: O(N^2)
## Notes:: The max area rectangle using stacks is used for O(N^2); instead of column cumsum, you would store the number of contiguous ones.
## Bookmarked:: Yes

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        m = len(A)
        if m == 0: return 0
        n = len(A[0])
        if n == 0: return 0
    
        cumsum = [[0] * n]
        for ix in range(m):
            sums = []
            for jx in range(n):
                sums.append(A[ix][jx] + cumsum[-1][jx])
            cumsum.append(sums)
        
        maxarea = 0
        for row1 in range(m+1):
            for row2 in range(row1 + 1, m + 1):
                all_ones_vertically = [
                    int(cumsum[row2][jx] - cumsum[row1][jx] >= (row2-row1))
                    for jx in range(n)
                ]
                max_horizontal = 0
                cur = 0
                for jx in range(n):
                    if all_ones_vertically[jx] == 0:
                        cur = 0
                        continue
                    cur += 1
                    max_horizontal = max(max_horizontal, cur)
                
                maxarea = max(maxarea, max_horizontal * (row2 - row1))
        return maxarea
                

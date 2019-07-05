## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/spiral-order-matrix-ii/
## Topic:: Arrays
## Sub-topic:: Simple iteration
## Difficulty:: Medium
## Approach:: Set the top, bottom, left, right, direction. Depending on these, keep moving. Update boundaries
## Notes:


class Solution:
    # @param A :: integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        n = A
        matrix = [[0] * n for _ in range(n)]
        top, left = 0, 0
        bottom, right = n - 1, n - 1

        direction = 0
        k = 1
        while top <= bottom and left <= right:
            if direction % 4 == 0:  # right
                for p in range(left, right + 1, 1):
                    matrix[top][p] = k
                    k += 1
                top += 1
            elif direction % 4 == 1:  # bottom
                for p in range(top, bottom + 1, 1):
                    matrix[p][right] = k
                    k += 1
                right -= 1
            elif direction % 4 == 2:
                for p in range(right, left - 1, -1):
                    matrix[bottom][p] = k
                    k += 1
                bottom -= 1
            elif direction % 4 == 3:
                for p in range(bottom, top - 1, -1):
                    matrix[p][left] = k
                    k += 1
                left += 1
            direction += 1
        return matrix
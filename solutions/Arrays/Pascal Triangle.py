## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/pascal-triangle/
## Topic:: Arrays
## Sub-topic:: Simple iteration, Combinations, Dynamic Programming
## Difficulty:: Easy
## Approach:: nCr = (n-1)Cr + (n-1)C(r-1)
## Time complexity:: O(n)
## Space complexity:: O(1)
## Notes:: Pascal's triangle is [[0C0], [1C0, 1C1], [2C0, 2C1, 2C2], ...]


class Solution:
    # @param A :: integer
    # @return a list of list of integers
    def solve(self, A):
        n = A
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        matrix = [[1], [1, 1]]
        for row in range(2, n):
            vals = [1]
            for col in range(1, row):
                vals.append(matrix[row-1][col-1] + matrix[row-1][col])
            vals.append(1)
            matrix.append(vals)
        return matrix
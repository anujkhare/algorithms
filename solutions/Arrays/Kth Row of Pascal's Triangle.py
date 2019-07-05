## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
## Topic:: Arrays
## Sub-topic:: Simple iteration, Combinations, Dynamic Programming
## Difficulty:: Easy
## Approach:: nCr = (n-1)Cr + (n-1)C(r-1)
## Time complexity:: O(n)
## Space complexity:: O(1)
## Notes:: Pascal's triangle is [[0C0], [1C0, 1C1], [2C0, 2C1, 2C2], ...]


class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        n = A
        matrix = [[1], [1, 1]]

        if n < 2:
            return matrix[n - 1]

        prev = matrix[1]

        for r in range(2, n + 1):
            cur = [1]
            for c in range(1, r):
                cur.append(prev[c - 1] + prev[c])
            cur.append(1)
            prev = cur
        return prev

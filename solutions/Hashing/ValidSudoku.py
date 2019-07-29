## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/valid-sudoku/
## Topic:: Hashing
## Sub-topic:: Search
## Difficulty:: Medium
## Approach:: Just store the numbers seen so far for row, col, and cell
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes::

import collections


class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        rows = [collections.defaultdict(int) for _ in range(9)]
        cols = [collections.defaultdict(int) for _ in range(9)]
        cells = [collections.defaultdict(int) for _ in range(9)]
        
        if len(A) != 9 or len(A[0]) != 9:
            return 0

        for row in range(9):
            for col in range(9):
                cell = (row // 3) * 3 + col // 3
                val = A[row][col]
                if val == '.': continue
                if rows[row][val] > 0: return 0
                if cols[col][val] > 0: return 0
                if cells[cell][val] > 0: return 0
                rows[row][val] = 1
                cols[col][val] = 1
                cells[cell][val] = 1
        return 1
                

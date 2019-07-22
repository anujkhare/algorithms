## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/queen-attack/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: For each row/col/diag, maintain the (hasQueen, minPos, maxPos) tuple; if no queen: add 0, else if b/w min and max: add 2 else 1;
## Time complexity:: O(MN)
## Space complexity:: O(MN)
## Notes:: Be careful that queens can't jump over each other!!
## Bookmarked:: Yes

import collections
 
class Solution:
    def queen_right_bottom(self, A):
        m, n = len(A), len(A[0])
        count = [[0] * n for _ in range(m)]
        
        queen_top = [False] * n
        queen_diag1 = [[False] * (n) for _ in range(m)]
        queen_diag2 = [[False] * (n+1) for _ in range(m)]
        for ix in range(m):
            queen_left = False
            for jx in range(n):
                count[ix][jx] += int(queen_left)
                count[ix][jx] += int(queen_top[jx])
                count[ix][jx] += int(queen_diag1[ix-1][jx-1]) if ix > 0 and jx > 0 else 0 # 0 is left of this
                count[ix][jx] += int(queen_diag2[ix-1][jx+1]) if ix > 0 and jx < n-1 else 0
 
                queen_diag1[ix][jx] = queen_diag1[ix-1][jx-1] if ix > 0 and jx > 0 else 0
                queen_diag2[ix][jx] = queen_diag2[ix-1][jx+1] if ix > 0 and jx < n-1 else 0
                
                if A[ix][jx] == '0':
                    continue
                queen_left = True
                queen_top[jx] = True
                queen_diag1[ix][jx] = 1
                queen_diag2[ix][jx] = 1
 
        # print(queen_diag1)
        # print(queen_diag2)
        return count
 
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        m = len(A)
        if m == 0: return [[]]
        n = len(A[0])
        if n == 0: return [[]]
        
        counts = self.queen_right_bottom(A)
        counts_r = self.queen_right_bottom([a[::-1] for a in A[::-1]])
        counts_r = [c[::-1] for c in counts_r[::-1]]
        for ix in range(m):
            for jx in range(n):
                counts[ix][jx] += counts_r[ix][jx]
        # print(counts)
        return counts

## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/matrix-search/
## Topic:: Binary Search
## Sub-topic:: Matrix
## Difficulty:: Easy
## Approach:: Think as array, convert index to row, col
## Time complexity:: O(log(M+N))
## Space complexity:: O(1)
## Notes:: This solution is too complex

class Arr:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __len__(self):
        return self.size

    @property
    def size(self):
        if self.m == 0:
            return 0
        return self.m * self.n
    
    @property
    def m(self):
        return len(self.matrix)
    
    @property
    def n(self):
        return len(self.matrix[0])
    
    def __getitem__(self, ix):
        if ix >= self.size:
            return None
        m, n = self.m, self.n
        row = ix // n
        col = ix % n
        
        return self.matrix[row][col]
        

class Solution:
    def bsearch(self, arr, target):
        lo, hi = 0, len(arr)
        mid = 0

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > target:
                hi = mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                break
        
        if lo >= hi or arr[mid] != target:
            return 0
        return 1
        
    def searchMatrix(self, A, B):
        matrix = Arr(A)
        return self.bsearch(matrix, B)


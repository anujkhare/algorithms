## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/sub-matrices-with-sum-zero/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: For 1D, use a hash map and store count for each sum; fix pair of rows to reduce matrix to 1D.
## Time complexity:: O(N^3)
## Space complexity:: O(N^2)
## Notes::
## Bookmarked:: Yes

class Solution:
    def colcumsums(self, arr):
        sums = []
        n = len(arr[0])
        prev = [0] * n
        
        for ix in range(len(arr)):
            cur = []
            for jx in range(n):
                cur.append(arr[ix][jx] + prev[jx])
            prev = cur
            sums.append(cur)
        return sums

    # @param A : list of list of integers
        # @return an integer
    def solve(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return 0
        m, n = len(A), len(A[0])
        
        col_cumsums = self.colcumsums(A)
        answer = 0
        
        # iterate over pair of rows
        for row1 in range(m):
            for row2 in range(row1, m):
                counts = {0: 1}
                cumsum = 0
                for col in range(n):
                    prev = col_cumsums[row1 - 1][col] if row1 > 0 else 0
                    cumsum += (col_cumsums[row2][col] - prev)
                    
                    c = counts.get(cumsum, 0)
                    answer += c
                    counts[cumsum] = c + 1
        return answer
        
        # iterate over columns, check if how many times the same cumsum has appeared

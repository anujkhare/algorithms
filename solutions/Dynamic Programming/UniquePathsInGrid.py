## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/unique-paths-in-a-grid/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: f(i, j) = f(i-1, j) + f(i, j-1)
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes::
## Bookmarked:: No

class Solution:
    # @param A : list of list of integers
        # @return an integer
    def uniquePathsWithObstacles(self, A):
        m = len(A)
        n = len(A[0])
        num_paths = [[0] * n for _ in range(m)]
        for ix in range(m):
            for jx in range(n):
                if A[ix][jx] == 1:
                    num_paths[ix][jx] = 0
                    continue

                if ix == 0 and jx == 0:
                    num_paths[ix][jx] = 1
                    continue
                if ix == 0:
                    num_paths[ix][jx] = num_paths[ix][jx-1]
                    continue
                if jx == 0:
                    num_paths[ix][jx] = num_paths[ix-1][jx]
                    continue

                num_paths[ix][jx] = num_paths[ix-1][jx] + num_paths[ix][jx-1]

        return num_paths[-1][-1]

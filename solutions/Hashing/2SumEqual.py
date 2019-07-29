## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/equal/
## Topic:: Hashing
## Sub-topic:: Search
## Difficulty:: Medium
## Approach:: Keep storing sum to ind
## Time complexity:: O(N^2)
## Space complexity:: O(N^2)
## Notes:: 

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        l = len(A)
        if l < 4:
            return []
        
        sum_to_ind = {}
        smallest_sol = None
        for ix in range(l):
            for jx in range(ix + 1, l):
                s = A[ix] + A[jx]
                if s in sum_to_ind:
                    sol = sum_to_ind[s] + [ix, jx]
                    if len(set(sol)) < 4:
                        continue

                    if smallest_sol is None or sol < smallest_sol:
                        smallest_sol = sol
                sum_to_ind[s] = [ix, jx]
        return smallest_sol or []

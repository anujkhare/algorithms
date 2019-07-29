## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/sliding-window-maximum/
## Topic:: Queue
## Sub-topic:: Deque
## Difficulty:: Medium
## Approach:: Maintain deque in the same order as the array; when inserting, remove all elements smaller than the cur number from the right;
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

import collections


class Solution:
    def _insert(self, q, ix, a):
        while len(q) > 0:
            val, pos = q[-1]
            if val <= a:
                q.pop()
            else:
                break
        q.append((a, ix))
    
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        q = collections.deque()
        w = B
        
        if len(A) <= w:
            return [max(A)]

        res = []
        for ix in range(len(A)):
            if len(q) > 0 and ix - w >= q[0][1]:
                q.popleft()
            self._insert(q, ix, A[ix])
            if ix >= w - 1:
                res.append(q[0][0])
        return res

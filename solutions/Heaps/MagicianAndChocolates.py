## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/magician-and-chocolates/
## Topic:: Heaps
## Sub-topic:: Min Heap
## Difficulty:: Easy
## Approach:: Simple heapify followed by insert
## Time complexity:: O(NlogN)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: No

import heapq


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        if len(B) == 0:
            return 0

        heap = [-b for b in B]  # to make it a max-heap
        heapq.heapify(heap)

        total = 0
        ix = 0
        while ix < A:
            ix += 1

            top = -heapq.heappop(heap)
            total += top
            new_top = top//2
            if new_top != 0:
                heapq.heappush(heap, -new_top)
            if len(heap) == 0:
                break

        return total

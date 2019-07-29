## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/distinct-numbers-in-window/
## Topic:: Heaps
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: Sort both arrays, maintain a max heap with the next largest sum pair; insert next based on the current; maintain map to prevent duplicates
## Time complexity:: O(NlogN)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: Yes

import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        A, B = sorted(A, reverse=True), sorted(B, reverse=True)

        heap = [(-A[0] - B[0], 0, 0)]
        results, visited = [], set()
        for ix in range(n):
            s, p1, p2 = heapq.heappop(heap)
            results.append(-s)
            visited.add((p1, p2))

            if p1 + 1 < n and (p1 + 1, p2) not in visited:
                heapq.heappush(heap, (-A[p1 + 1] - B[p2], p1 + 1, p2))
                visited.add((p1 + 1, p2))
            if p2 + 1 < n and (p1, p2 + 1) not in visited:
                heapq.heappush(heap, (-A[p1] - B[p2 + 1], p1, p2 + 1))
                visited.add((p1, p2 + 1))

        return results

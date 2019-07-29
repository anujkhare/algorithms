## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/distinct-numbers-in-window/
## Topic:: Hashing
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Just maintain count in a dict
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: No

import collections

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, arr, k):
        counts = collections.defaultdict(int)
        result = []
        
        for ix in range(len(arr)):
            counts[arr[ix]] = counts[arr[ix]] + 1
            
            if ix >= k:
                counts[arr[ix-k]] = counts[arr[ix-k]] - 1
                if counts[arr[ix-k]] == 0:
                    counts.pop(arr[ix-k])
            
            if ix + 1 >= k:
                result.append(len(counts))

        return result

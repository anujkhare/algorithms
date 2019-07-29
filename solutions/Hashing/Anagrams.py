## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/anagrams/
## Topic:: Hashing
## Sub-topic:: Key formation
## Difficulty:: Easy
## Approach:: Just sort each word to form it's key!
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

import collections


class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        results = collections.defaultdict(list)
        
        for ix, a in enumerate(A):
            key = ''.join(sorted(a))
            results[key].append(ix + 1)
        
        return sorted(results.values())

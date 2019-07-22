## Website:: Leetfree
## Link:: https://leetfree.com/problems/longest-consecutive-sequence.html
## Topic:: Hashing
## Sub-topic:: Strings
## Difficulty:: Hard
## Approach:: Hash all the numbers; iterate over all numbers considering them as the starting point; if the prev number exists in the array, stop; keep adding one and trying to create a longer sequence.
## Time complexity:: O(2*N)
## Space complexity:: O(N)
## Notes:: The intuition should come from the fact that you can do an O(range) algorithm by iterating over all numbers between the min and the max and checking in the hash.


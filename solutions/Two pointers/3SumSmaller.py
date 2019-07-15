## Website:: Leetfree
## Link:: https://leetfree.com/problems/longest-substring-with-at-most-two-distinct-characters.html
## Topic:: Two pointers
## Sub-topic:: 3 pointers
## Difficulty:: Medium
## Approach:: Sort; reduce to 2PointersSmaller by fixing the largest pointer; if sum is larger than target, p2--, else add all the pairs between [p1+1, p2] to count, p1++; repeat.
## Time complexity:: O(N^2)
## Space complexity:: O(1)
## Notes:: 



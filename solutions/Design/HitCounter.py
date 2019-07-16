## Website:: Leetfree
## Link:: https://leetfree.com/problems/design-hit-counter.html
## Topic:: Design
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Maintain a dequeue with timestamp and counts, a separate counter. At each hit, remove all the elements which aren't within a 300 window and then insert
## Time complexity:: O(1) query, O(300) for hit.
## Space complexity:: O(300)
## Notes:: You can optimize
## Bookmarked:: No


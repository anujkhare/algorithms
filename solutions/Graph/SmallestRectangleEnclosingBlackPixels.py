## Website:: Leetfree
## Link:: https://leetfree.com/problems/smallest-rectangle-enclosing-black-pixels.html#approach-3-binary-search-accepted
## Topic:: Graph, Binary Search
## Sub-topic:: BFS/DFS, binary search
## Difficulty:: Hard
## Approach:: BFS based solution is easy but slow. Since there is only one connected component, you can binary search for the top and bottom rows which have at least one black pixel. Instead of pre-computing the projections, you can do that lazily.
## Time complexity:: O(MlogN + NlogM)
## Space complexity:: O(1)
## Notes:: Lazy computation while doing bsearch is very interesting!
## Bookmarked:: Yes

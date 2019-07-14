## Website:: Geeks4Geeks
## Link:: http://www.cs.umd.edu/~soheil/cmsc351/files/22-1-allsp.pdf
## Topic:: Graph
## Sub-topic:: Shortest Path
## Difficulty:: Medium
## Approach:: At each step, the SP[u] by considering all incoming edges. Repeat for |V| times. This works since at step `i` you find the shortest paths to the vertices which are at most `i` steps (edges) apart.
## Time complexity:: O(VE)
## Space complexity:: O(E)
## Notes:: This also works for edges with negative weights, unlike Dijkstra's algorithm


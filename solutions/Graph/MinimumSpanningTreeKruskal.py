## Website:: Geeks4Geeks
## Link:: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
## Topic:: Graph
## Sub-topic:: MST, Greedy, Union Find
## Difficulty:: Medium
## Approach:: Greedily pick the smallest weight edge until you have N-1 edges. If the edge picked forms a cycle with the existing sub-tree, discard it. Use Union Find to detect the cycles.
## Time complexity:: O(E logV + E logE) = O(E logE) = O(E logV)  [since E = O(V^2)]
## Space complexity:: O(V + E)
## Notes:: 

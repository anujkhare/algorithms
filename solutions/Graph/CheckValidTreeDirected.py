## Website:: Leetfree
## Link:: https://leetfree.com/problems/graph-valid-tree.html
## Topic:: Graph
## Sub-topic:: Tree
## Difficulty:: Easy
## Approach:: If more than (n-1) edges, fail. Find root: the node with in-degree 0. If not found, fail. If multiple roots (forest), fail. Do a BFS. If you don't visit all nodes, fail. If you visited a node twice, fail.
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: https://stackoverflow.com/questions/20556802/given-a-graph-to-detect-if-it-is-a-tree-or-not-in-directed-and-undirected-graphs

## Website:: Leetfree
## Link:: https://leetfree.com/problems/closest-binary-search-tree-value-ii.html
## Sub-topic:: BST, Heap, Two pointers
## Difficulty:: Hard
## Approach:: Find the value just greater than or equal to it. Then, use two pointers to iterate over the predec./succes. Maintain a stack to implement pre/suc.
## Time complexity:: O(logN + K)
## Space complexity:: O(logN)
## Notes:: Think of how you would do it in a sorted array. Iteration+Heap: O(NlogK). Instead, bisect_left + two pointers: O(logN + K). Implement the second one in a BST.
## Bookmarked:: Yes

## Website:: Interviewbit
## Link:: https://leetfree.com/problems/sentence-screen-fitting.html
## Topic:: Strings
## Sub-topic:: Greedy
## Difficulty:: Medium
## Approach:: Iterate over the rows. For each row, add ncol to the count. If you've cut a word, remove the last part of the word.
## Time complexity:: O(N*R) where N=len(str) and R=number of rows
## Space complexity:: O(N)
## Notes:: You can store the cumulative lengths of the words and do binary search on the lengths to reduce N->logN. https://medium.com/@rebeccahezhang/leetcode-418-sentence-screen-fitting-9d6258ce116e

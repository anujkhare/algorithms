## Website:: LeetFree
## Link:: https://leetfree.com/problems/minimum-window-subsequence.html
## Topic:: Dynamic Programming
## Sub-topic:: 2D
## Difficulty:: Hard
## Approach:: Start with the solution to see if T is a subsequence of S. Also, the minimum length of the substring assuming S_i is the last character. Whenever the last characters match, take min seqLen if you use this char in S vs if you don't use it. Maintain a minimum Take a global minimum. 
## Time complexity:: O(log(MN))
## Space complexity:: O(M) - length of the string S
## Notes:: 
## Bookmarked: No

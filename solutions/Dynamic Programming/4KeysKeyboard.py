## Website:: LeetFree
## Link:: https://leetfree.com/problems/4-keys-keyboard.html
## Topic:: Dynamic Programming
## Sub-topic:: 1D
## Difficulty:: Medium
## Approach:: f(n) = max(f(n-1) + 1, max(f(n-2-k) * (k+1)) for k >= 1)
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes:: This can be further reduced by observing the fact that there is a maximum number of Pastes that would be useful
## Bookmarked: No

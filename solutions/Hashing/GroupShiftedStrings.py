## Website:: Leetfree
## Link:: https://leetfree.com/problems/group-shifted-strings.html
## Topic:: Hashing
## Sub-topic:: Key formation
## Difficulty:: Medium
## Approach:: Find the hash of each string by making the first character an 'a'. Keep adding all the other strings to the same list.
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: Be careful while taking the differences, you need to account for the cyclic change (...x,y,z,a,b,c...)

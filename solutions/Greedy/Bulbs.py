## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/bulbs/
## Topic:: Greedy
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Go left to right and count
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 
## Bookmarked:: No

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        l = len(A)
        if l == 0:
            return 0
        flips = 0
        for s in A:
            if (flips + s) % 2 == 1:
                continue
            flips += 1
        return flips

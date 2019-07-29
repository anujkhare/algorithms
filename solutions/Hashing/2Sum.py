## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/2-sum/
## Topic:: Hashing
## Sub-topic:: Search
## Difficulty:: Easy
## Approach:: Hash the numbers as you go, if you find a pair, return
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes::

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        num_to_pos = {}
        for ix, num in enumerate(A):
            d = B - num
            if d in num_to_pos:
                return [num_to_pos[d], ix + 1]
            if num not in num_to_pos:
                num_to_pos[num] = ix + 1
        return []

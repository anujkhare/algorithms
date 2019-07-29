## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/diffk-ii/
## Topic:: Hashing
## Sub-topic:: Search
## Difficulty:: Easy
## Approach:: hash and check
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes::

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        nums = set()
        for num in A:
            if num - B in nums:
                return 1
            if num + B in nums:
                return 1
            nums.add(num)
        return 0

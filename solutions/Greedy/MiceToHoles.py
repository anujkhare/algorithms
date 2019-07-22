## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/assign-mice-to-holes/
## Topic:: Greedy
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: The leftmost mouse will go the leftmost hole and so on; Sort both and find the max travel time
## Time complexity:: O(NlogN)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: No

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        la, lb = len(A), len(B)
        if la != lb:
            raise
        if la == 0:
            return 0
        A = sorted(A)
        B = sorted(B)
        time = 0
        for a, b in zip(A, B):
            time = max(time, abs(a-b))
        return time

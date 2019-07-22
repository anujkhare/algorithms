## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/bulbs/
## Topic:: Greedy
## Sub-topic:: 
## Difficulty:: Easy
## Approach:: Count increasing sequence from left and from the right, take max at each point;
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: No

class Solution:
    def candy_one_sided(self, A):
        l = len(A)
        if l == 0:
            return []
        ans = [1]
        for ix in range(1, l):
            if A[ix] > A[ix-1]:
                ans.append(ans[-1] + 1)
            else:
                ans.append(1)
        return ans

    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        l2r = self.candy_one_sided(A)
        r2l = self.candy_one_sided(A[::-1])[::-1]
        ans = 0
        for ix in range(len(A)):
            ans += max(l2r[ix], r2l[ix])
        return ans
            

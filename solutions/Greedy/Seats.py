## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/seats/
## Topic:: Greedy
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Find median, move everyone close to the median, no one will jump over another, so you know the order
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: 
## Bookmarked:: Yes

class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        div = 10000003
        lst = []
        for i in range(len(A)):
            if A[i] == "x":
                lst.append(i)
        if len(lst) <= 1:
            return 0
            
        med = len(lst)/2
        lc = 0
        rc = 0
        for i in range(med, -1, -1):
            lc += lst[med] - lst[i] - (med - i)
        
        for i in range(med + 1, len(lst)):
            rc += lst[i] - lst[med] - (i-med)
            
        return (lc + rc) % div

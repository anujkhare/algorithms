## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/points-on-the-straight-line/
## Topic:: Hashing
## Sub-topic:: Key formation
## Difficulty:: Hard
## Approach:: Either hash the lines (slope and intercept), but too much floating point error possible; an easier way is to store just the slope for each given point and see how many other points form a line with the same slope
## Time complexity:: O(N^2)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: Yes

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        n = len(A)
        if (n<=2):
            return n
        m = 0 #result value
        for i in range(n):
            l = {}  #every time reset the dict
            dup = 1 #count the duplicates
            for j in range(n):
                if (A[i]==A[j] and B[i]==B[j] and i!=j):        
                    dup+=1  #count duplicates
                elif i!=j :
                    if (A[i]==A[j]):  #vertical line
                        l['v'] = l.get('v',0) + 1
                    elif (B[i]==B[j]): # horizontal line
                        l['h'] = l.get('h',0) + 1
                    else:   #regular slope
                        slope = 1.0*(B[i]-B[j])/(A[i]-A[j])
                        l[slope] = l.get(slope,0)+1
            if (len(l)>0): 
                m = max(m,max(l.values())+dup)
            else: #if all points are duplicates, l is empty.
                m = max(m,dup)
        return m

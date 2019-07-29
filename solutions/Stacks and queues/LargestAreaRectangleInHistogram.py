## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/sliding-window-maximum/
## Topic:: Stacks
## Sub-topic:: 
## Difficulty:: Hard
## Approach:: Maintain stack; while inserting, remove all elements larger than it; while removing, check for the rectangles formed with those heights.
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: The optimization for O(n) is slightly tricky! You need to notice that you can look at the options "lazily"
## Bookmarked:: Yes

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        st = []
        l = len(A)
        if l == 0:
            return 0
        
        maxarea = 0
        for ix, a in enumerate(A):
            curwidth = 0
            # replace all the bars taller than the cur height with cur
            while len(st) > 0 and st[-1][0] >= a:
                h, w, jx = st.pop()
                curwidth += w
                # check if the desired region could start from this bar
                maxarea = max(maxarea, h * curwidth)
        
            curwidth += 1
            st.append((a, curwidth, ix))
        
        # Check rectangles starting from all the remaining bars
        # Note that all the remaining bars would be in increasing order
        curwidth = 0
        while len(st) > 0:
            h, w, _ = st.pop()
            curwidth += w
            maxarea = max(maxarea, h * curwidth)
        
        return maxarea

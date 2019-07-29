## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/rain-water-trapped/
## Topic:: Stacks
## Sub-topic:: Tricky
## Difficulty:: Medium
## Approach:: Go left to right and keep adding the water; once done, the pillars on the left of a larger pillar don't matter anymore!
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 
## Bookmarked:: Yes


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        st = []
        water = 0
        for ix, a in enumerate(A):
            curlevel = 0
            # print(st)
            
            while len(st) > 0 and st[-1][1] <= a:
                ind, h = st.pop()
                water += max(0, h - curlevel) * (ix - ind - 1)
                # print(h, water, curlevel)
                curlevel = h
            
            # calculate the water till the larger pillar before it
            if len(st) > 0 and st[-1][1] > a:
                ind, h = st[-1]
                water += (a - curlevel) * (ix - ind - 1)
            
            # print(water)
            # push this guy
            st.append((ix, a))
        return water

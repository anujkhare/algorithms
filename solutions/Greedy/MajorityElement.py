## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/majority-element/
## Topic:: Greedy
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Maintain a counter for the current element and inc/dec based on the new elements; If it reaches 0, reset.
## Time complexity:: O(N)
## Space complexity:: O(1)
## Notes:: The easier way is to hash!
## Bookmarked:: No

import

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        l = len(A)
        if l == 0:
            return 0
        count1, count2 = 0, 0
        n1, n2 = None, None
        for a in A:
            if n1 is None: n1 = a
            if n2 is None: n2 = a

            if n1 == a:
                count1 += 1
                continue
            if n2 == a:
                count2 += 1
                if count2 > count1:
                    count1, count2 = count2, count1
                    n1, n2 = n2, n1
                continue
            n2 = a
            count2 = 1
        return n1

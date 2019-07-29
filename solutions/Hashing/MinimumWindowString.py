## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/window-string/
## Topic:: Hashing
## Sub-topic:: Search, two pointers
## Difficulty:: Easy
## Approach:: Two pointers, keep moving right if you have more than required characters
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if B == '' or A == '':
            return ''

        # Get the counts of each char required
        required = {}
        for c in B:
            required[c] = required.get(c, 0) + 1
        
        # Find windows which have these counts
        pstart, pend = 0, 0
        minlen, window = float('inf'), ''

        while pend < len(A):
            c = A[pend]
    
            # Update the required count of this char
            if c in required:
                required[c] -= 1
                
                # Try to move pstart such that the window still has all
                while pstart <= pend:
                    if A[pstart] not in required:
                        pstart += 1
                        continue
                    if required[A[pstart]] < 0:
                        required[A[pstart]] += 1
                        pstart += 1
                    else:
                        break

            # Check if this window has all we need, if so, update
            if all(v <= 0 for v in required.values()):
                window_len = pend - pstart + 1
                if window_len < minlen:
                    minlen = window_len
                    window = A[pstart: pend + 1]

            pend += 1

        return window

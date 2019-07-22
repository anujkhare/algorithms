## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/arrange-ii/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: f(1...n, k) = min_i f(1...i, 1) + f(i+1...n, k-1)
## Time complexity:: O(NK)
## Space complexity:: O(N)
## Notes:: This is like rod cutting where the cost of cutting needs to be calculated as well
## Bookmarked:: Yes

class Solution:
    def arrange(self, arr, K):
        n = len(arr)
        
        if n == 0:
            return 0
        if K == 0:
            return -1
        if K > n:
            return -1

        w, b = [0] * n, [0] * n
        for ix, color in enumerate(arr):
            w[ix] = w[ix-1] if ix > 0 else 0
            b[ix] = b[ix-1] if ix > 0 else 0
            if color == 'W': w[ix] += 1
            if color == 'B': b[ix] += 1

        minsums_prev = [white * black for white, black in zip(w, b)]  # for 1 stable
        for k in range(2, K+1):
            minsums_cur = [0] * n
            for ix in range(n):
                mincost = float('inf')
                if ix + 1 < k:  # number of horses is less than number of stables
                    continue
                # choose the mincost starting point of the last stable
                for jx in range(ix):  # less than ix
                    cost_last_stable = (w[ix] - w[jx]) * (b[ix] - b[jx])
                    cost =  cost_last_stable + minsums_prev[jx] # mincost for the prefix, cost of last stable
                    mincost = min(mincost, cost)
                
                minsums_cur[ix] = mincost

            minsums_prev = minsums_cur
            # print(minsums_prev)

        return minsums_prev[-1]

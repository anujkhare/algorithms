## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/coin-sum-infinite/
## Topic:: Dynamic Programming
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: f(N, {c1...cs}) = f(N, {c1...cs-1}) + f(N-cs, {c1...cs})
## Time complexity:: O(NS)
## Space complexity:: O(N)
## Notes:: When you pick a coin, you need to make sure that the maximum valuecoin value that will be used for this sum total is equal to that coin. This way, you can ensure non-overlapping sub-problems. Otherwise, you have overlapping sub-problems, which sucks, totally.
## Bookmarked:: No

MOD = int(1000007)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, arr, num):
        if len(arr) == 0:
            return 0
        
        ways_prev = [0] * (num + 1)  # start with sum = 0
        ways_prev[0] = 1

        for cur_val in arr:
            ways_cur = [0] * (num + 1)
            
            for n in range(num + 1):
                if cur_val > n:  # this coin is too big
                    ways_cur[n] = ways_prev[n]
                    continue
                ways_cur[n] = ways_prev[n] + ways_cur[n-cur_val]
            
            ways_prev = ways_cur
            
        return ways_prev[num] % MOD

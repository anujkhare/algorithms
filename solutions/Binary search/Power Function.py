## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/add-one-to-number/
## Topic:: Binary Search, Divide and Conquer
## Sub-topic:: Guess solution
## Difficulty:: Medium
## Approach:: a * b % d = ((a % d) * (b % d)) % d
## Time complexity:: O(log(N))
## Space complexity:: O(1)
## Notes:: Just keep dividing and memorizing. Do it iteratively to save space

class Solution:
    def pow_helper(self, x, n, d, mem):
        if (x, n) in mem:
            return mem[(x, n)]
            
        if x == 0: return 0
        if n == 0: return 1
        if n == 1: return x % d

        p1 = n // 2
        p2 = n - p1
        ans = (self.pow_helper(x, p1, d, mem) % d * self.pow_helper(x, p2, d, mem) % d ) % d
        mem[(x, n)] = ans
        return ans

    def pow(self, x, n, d):
        return self.pow_helper(x, n, d, {})

## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/4-sum/
## Topic:: Hashing
## Sub-topic:: Simple
## Difficulty:: Hard
## Approach:: Hash the sums of pairs of numbers in the array and store the inds; for each sum, check if pair sum exists, validate that the 4 indices are unique, add to the final list; Finally, sort and return the tuples..
## Time complexity:: O(N^2)
## Space complexity:: O(N^2)
## Notes::

import collections
import itertools


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        sum_to_inds = collections.defaultdict(list)
        l = len(A)
        if l == 0: return []
        
        for ix in range(l):
            for jx in range(ix + 1, l):
                s = A[ix] + A[jx]
                sum_to_inds[s].append((ix, jx))
        
        # print(sum_to_inds)
        results = []
        for s, inds_list in sum_to_inds.items():
            s2 = B - s
            if s2 not in sum_to_inds:
                continue

            l, r = sum_to_inds[s], sum_to_inds[s2]
            for ix, jx in itertools.product(range(len(l)), range(len(r))):
                inds = list(l[ix]) + list(r[jx])
                if len(set(inds)) < 4: continue
                nums = [A[ix] for ix in inds]
                results.append(tuple(sorted(nums)))
            
            sum_to_inds.pop(s)
            if s != s2:
                sum_to_inds.pop(s2)

        results = sorted(set(results))
        return results

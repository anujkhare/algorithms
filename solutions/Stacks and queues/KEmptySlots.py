## Website:: Leetfree
## Link:: https://leetfree.com/problems/k-empty-slots.html
## Topic:: Queues
## Sub-topic:: Dequeue, MinQueue
## Difficulty:: Hard
## Approach:: Maintain a "MinQueue": a data structure to maintain the minimum value in a sliding window.
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: A simpler solution of O(NlogN) also exists by inserting in a sorted order.
## Bookmarked:: Yes


from collections import deque
class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]

class Solution(object):
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        window = MinQueue()
        ans = len(days)

        for i, day in enumerate(days):
            window.append(day)
            if k <= i < len(days) - 1:
                window.popleft()
                if k == 0 or days[i-k] < window.min() > days[i+1]:
                    ans = min(ans, max(days[i-k], days[i+1]))

        return ans if ans <= len(days) else -1

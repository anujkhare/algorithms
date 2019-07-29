## Website:: Leetfree, Interviewbit
## Link:: https://www.interviewbit.com/problems/merge-k-sorted-lists
## Topic:: Heaps
## Sub-topic:: Min Heap
## Difficulty:: Medium
## Approach:: Insert the first element of all lists into a min heap along with some kind of a pointer. Pop, move the pointer, continue.
## Time complexity:: O(N logK) where N is the number of elements in the longest list.
## Space complexity:: O(K) extra space (besides output array)
## Notes:: Could also do with just K pointers, but the time complexity would be O(NK)
## Bookmarked:: No

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        k = len(A)
        if k == 0:
            return 
        head = ListNode(0)
        
        heap = [(node.val, node) for node in A if node is not None]
        heapq.heapify(heap)
        
        p = head
        while len(heap) > 0:
            _, node = heapq.heappop(heap)
            p.next = node
            p = node
            
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            node.next = None

        return head.next

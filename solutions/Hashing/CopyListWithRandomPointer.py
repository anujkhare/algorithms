## Website:: Interviewbit
## Link:: https://www.interviewbit.com/problems/copy-list/
## Topic:: Hashing
## Sub-topic:: Key formation
## Difficulty:: Medium
## Approach:: DFS, hash the nodes to prevent duplication
## Time complexity:: O(N)
## Space complexity:: O(N)
## Notes:: 

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return head
        
        orig_node_to_ix = {}
        L = 0
        p = head
        while p:
            orig_node_to_ix[p] = L
            p, L = p.next, L + 1

        new_head = RandomListNode(head.label)
        orig = head.next
        prev = new_head

        random_pointers = [orig_node_to_ix.get(head.random, None)]
        nodes = [new_head]

        while orig:
            prev.next = RandomListNode(orig.label)
            prev = prev.next
    
            nodes.append(prev)
            random_pointers.append(orig_node_to_ix.get(orig.random, None))
            orig = orig.next
        
        assert len(random_pointers) == L
        assert len(nodes) == L
        
        for ix in range(L):
            pointer = random_pointers[ix]
            node1 = nodes[ix]
            if pointer is None or pointer % (L + 1) == L:
                node1.random = None
                continue
            node1.random = nodes[pointer % (L + 1)]
        
        return new_head

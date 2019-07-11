## Website:: Interviewbit
## Link:: https://leetfree.com/problems/minimum-window-subsequence.html
## Topic:: String, Trie, Tree
## Sub-topic:: Trie, String
## Difficulty:: Medium
## Approach:: Construct a trie, find the shortest unique prefix
## Time complexity:: O(N.L) N: words, L: length
## Space complexity:: O(N.L)
## Notes:: 
## Bookmarked: Yes

import collections


class TrieNode:
    def __init__(self, val: str) -> None:
        if len(val) > 1:
            raise ValueError
        self.val = val
        self.children = {}
        self.leaf_count = 1

    def __repr__(self) -> str:
        return '{}-{}'.format(self.val, self.leaf_count)

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode('')
    
    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        cur = self.root
        for char in word:
            if char in cur.children:  # already exists
                cur.children[char].leaf_count += 1  # there are two words below it now!
            else:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]

    def print_level_order(self):
        q = collections.deque()
        q.append(self.root)
        values = []
        
        while len(q) > 0:
            node = q.popleft()
            if node is None:
                continue
            values.append(str(node))
            for child in node.children.values():
                q.append(child)
        return values
    
    def unique_prefix(self, word: str) -> str:
        cur = self.root
        if len(word) == 0:
            return ''

        for ix, char in enumerate(word):
            if char not in cur.children:
                raise ValueError('missing word: {}, char: {}'.format(word, char))
            
            cur = cur.children[char]
            
            if cur.leaf_count == 1:
                return word[:ix+1]
        
        raise ValueError('Two duplicate words!: {}'.format(word))

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        if len(A) == 0:
            return []
        trie = Trie()
        for word in A:
            trie.insert(word)
        
        # print(trie.print_level_order())
        prefixes = []
        for word in A:
            prefixes.append(trie.unique_prefix(word))
        return prefixes
        

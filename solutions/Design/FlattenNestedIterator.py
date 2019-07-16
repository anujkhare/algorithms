## Website:: LeetCode
## Link:: https://leetcode.com/problems/flatten-nested-list-iterator/
## Topic:: Design
## Sub-topic:: 
## Difficulty:: Medium
## Approach:: Recursively define a nested iterator
## Time complexity:: O(1)
## Space complexity:: O(1)
## Notes::
## Bookmarked:: No


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        elements = []
        for item in nestedList:
            if not item.isInteger():
                iterator = NestedIterator(item.getList())
                if iterator.hasNext():  # remove any empty sub-lists, recursively!
                    elements.append(iterator)
            else:
                elements.append(item.getInteger())
        self.elements = elements
        self.l = len(elements)
        self.ix = 0

    def next(self):
        """
        :rtype: int
        """
        elem = self.elements[self.ix]
        if isinstance(elem, NestedIterator):
            val = elem.next()
            if not elem.hasNext():
                self.ix += 1
            return val
        self.ix += 1
        return elem
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ix < self.l
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

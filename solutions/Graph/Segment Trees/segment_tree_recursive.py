## Website:: Self
## Link::
## Topic:: Graph
## Sub-topic:: Segment Tree
## Difficulty:: Medium
## Approach:: Recursively split the interval into two smaller intervals
## Time complexity:: insert: O(N logN), update: O(logN), query: O(logN)
## Space complexity:: O(2*N)
## Notes::
## Bookmarked: Yes
import collections


class Node:
	def __init__(self, start, end):
		self.left = None
		self.right = None
		self.sum = 0
		self.start = start
		self.end = end

class SegmentTreeR:
	def __init__(self, nums):
		self.nums = nums
		
		self.root = self._create_tree(nums, 0, len(nums)-1)
	
	def _create_tree(self, nums, start, end):
		if start == end:
			leaf = Node(start, end)
			leaf.sum = nums[start]
			return leaf
		if start > end:
			return None

		root = Node(start, end)		
		
		mid = (start + end) // 2
		root.left = self._create_tree(nums, start, mid)
		root.right = self._create_tree(nums, mid+1, end)
		
		root.sum = root.left.sum + root.right.sum
		return root
	
	def update(self, pos, val):
		def _update_helper(root, pos, val):
			if root is None:
				return
			
			# outside the interval
			start, end = root.start, root.end
			if pos < root.start or pos > root.end:
				return
			
			# leaf node case
			if root.start == root.end and root.start == pos:
				root.sum = val
				return
			
			# update recursively
			_update_helper(root.left, pos, val)
			_update_helper(root.right, pos, val)
			root.sum = root.left.sum + root.right.sum
			
		_update_helper(self.root, pos, val)
	
	def query(self, start, end):
		def _query_helper(root, start, end):
			# completely outside
			if root.start > end or root.end < start:
				return 0
			# completely contained: return the whole thing
			if root.start >= start and root.end <= end:
				return root.sum
			
			# overlapping, but not contained
			return _query_helper(root.left, start, end) +\
				   _query_helper(root.right, start, end)		
		
		return _query_helper(self.root, start, end)
		
	def levelorder(self):
		q = collections.deque()
		q.appendleft((self.root, 0))		
		while len(q) > 0:
			node, level = q.pop()
			if node is None: continue
			print(level, node.start, node.end, node.sum)
			q.appendleft((node.left, level+1))
			q.appendleft((node.right, level+1))
	
	def find_cumsum_ind(self, sum):
		def _helper(root, sum):
			# invalid cases, shouldn't happen
			if root is None: return None
			if sum > root.sum: return None

			# Found the correct leaf node!
			if root.start == root.end:
				if sum == 1: return root.start
				return None

			# Go left if sum is l_e than left node's sum
			if root.left and sum <= root.left.sum:
				return _helper(root.left, sum)
			else:
				s = root.left.sum if root.left else 0
				return _helper(root.right, sum - s)
		
		return _helper(self.root, sum)


if __name__ == '__main__':
	empty = [1] * 2
	stree = SegmentTreeR(empty)
	
	print(stree.find_cumsum_ind(1))
	stree.update(1, 0)
	print(stree.find_cumsum_ind(0))
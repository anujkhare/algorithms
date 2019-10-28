import math


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


class BinaryTree:
	def __init__(self, root_val):
		self.root = TreeNode(root_val)
	
	@classmethod
	def from_inorder(cls, arr):
		l = len(arr)
		if l == 0: return None

		h = math.log(l+1, 2)  # for fully balanced, l = 2**h - 1
		assert h == math.trunc(h)  # should provide inputs for the entire balanced tree
		
		root

	@classmethod
	def from_postorder(cls, arr):
		pass
		
	@classmethod
	def from_preorder(cls, arr):
		pass
	
	@classmethod
	def from_levelorder(cls, arr):
		pass

	def successor(self, node):
		pass
	
	def predecessor(self, node):
		pass
	
	def min_val(self, root):
		pass
	
	def max_val(self, root):
		pass
	
	def min_val_recursive(self, root):
		pass
		
	def max_val_recursive(self, root):
		pass

	def insert(self, val):
		pass
	
	def delete(self, val):
		pass
	
	@property
	def height(self, val):
		pass
	
	def inorder(self, root):
		pass
	
	def postorder(self, root):
		pass
	
	def levelorder(self, root):
		pass
	
	def inorder_iterative(self, root):
		pass
	
	def postorder_iterative(self, root):
		pass
	
	def levelorder_iterative(self, root):
		pass


def predecessor_with_stack(root):
	pass

def successor_with_stack(root):
	pass
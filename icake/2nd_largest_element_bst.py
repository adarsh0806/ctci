# Find the 2nd largest element in a BST
class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		self.value = value
		self.left = left
		self.right = right

	def insert_left(self, value):
		self.left = BinaryTree(value)
		return self.left

	def insert_right(self, value):
		self.right = BinaryTree(value)
		return self.right

	def largest(root):
		while root:
			if not root.right:
				return root.value
			root = root.right

	def second_largest(root):
		while root:
			if root.left and root.left:
				return largest(root.left)
			if root.right and not root.right.left and not not root.right.right:
				return root.value
			root = root.right	
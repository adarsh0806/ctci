class BTreeNode(object):
	"""docstring for BTreeNode"""
	def __init__(self, value):
		self.value = value
		self.right = right
		self.left = left

	def insert_left(self, value):
		self.left = BTreeNode(value)
		return self.left

	def insert_right(self, value):
		self.right = BTreeNode(value)
		return self.right

	def is_balanced(root):
		depths = []
		nodes = []
		# nodes has tuples of (node, depth)
		nodes.append((root, 0))

		while len(nodes):
			# pop the last element
			node, depth = nodes.pop()
			# if we are at a leaf node(no children)
			if not node.left and not node.right:
				if depth not in depths:
					depths.append(depth)
				if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
					return False
			else:
				if node.left:
					nodes.append((node.left, depth + 1))
				if node.right:
					nodes.append((node.right, depth + 1))	
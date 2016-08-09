# Binary Tree
# Naming conventions
# module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name
class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

	# set data
	def set_data(self, data):
		self.data = data

	# get data
	def get_data(self):
		return self.data

	# get left child
	def get_left(self):
		return self.left

	# get right child
	def get_right(self):
		return self.right


	def preorder(root, result):
		# DLR
		if not root:
			return
		result.append(root.data)
		preorder(root.left, result)
		preorder(root.right, result)


	def inorder(root, result):
		# LDR
		if not root:
			return
		inorder(root.left, result)
		result.append(root.data)
		inorder(root.right, result)

	def postorder(root, result):
		#LRD
		if not root:
			return
		postorder(root.right, result)
		postorder(root.left, result)
		result.append(root.data)

		
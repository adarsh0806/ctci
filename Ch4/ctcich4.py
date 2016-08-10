# 4.1 Check if a binary tree is balanced(heights of two subtrees of a node do not differ by more than 1)
import random

class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self, content):
		self.left = None
		self.right = None
		self.content = content
		self.depth = -1 # depth = -1 when its not been calculated yet

	def __str__(self):
		return '(' + str(self.left) + ' - ' + str(self.content) + ' - ' + str(self.right) + ')'


def depth(btree):
	if btree is None:
		return
	else:
		if btree.depth != -1:
			return btree.depth
		else:
			btree.depth = 1 + max(depth(btree.left), depth(btree.right))
			return btree.depth

bt = BinaryTree(random.randint(0, 9))
for c1 in xrange(0,3):
    bt2 = BinaryTree(random.randint(0, 9))
    bt2.left = bt
    bt = bt2
print bt.depth

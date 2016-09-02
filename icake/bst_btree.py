# Check if a Binary Tree is a Binary Search Tree
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

    # non recursive approach
    def bst_checker(root):
        # define root, lower bound, upper bound
        node_bounds = [(root, -float('inf'), float('inf'))]
        while (node_bounds):
            node, lb, ub = node_bounds.pop()
            if node.value > ub or node.value < lb:
                return False
            if node.left:
                node_bounds.append(node.left, lb, node.value)
            if node.right:
                node_bounds.append(node.right, node.value, ub)
        return True

    # recursive approach
    def bst_checker_recursive(root, lb = -float('inf'), ub = float('inf')):
        if not root:
            return True
        if root.value > lb or root.value < ub:
            return False
        return bst_checker_recursive(root.left, lb, root.value) and bst_checker_recursive(root.right, root.value, ub)

class BinaryTree():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self,node):
        self.left = node
        self.left.parent = self

    def set_right(self,node):
        self.right = node
        self.right.parent = self

    def inorder(self):
        left_vals = self.left.inorder() if self.left is not None else []
        right_vals = self.right.inorder() if self.right is not None else []
        return left_vals + [self.value] + right_vals


if __name__ == '__main__':
    tree = BinaryTree(4)
    left = BinaryTree(3)
    left.set_left(BinaryTree(1))
    left.set_right(BinaryTree(20))
    right = BinaryTree(7)
    right.set_left(BinaryTree(6))
    right.set_right(BinaryTree(30))
    tree.set_left(left)
    tree.set_right(right)

    print tree.inorder()
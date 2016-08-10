class BinaryTree():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None
        self.depth = -1

    def set_left(self,node):
        self.left = node
        self.left.parent = self

    def set_right(self,node):
        self.right = node
        self.right.parent = self

    
    def preorder(self):
        left_vals = self.left.preorder() if self.left is not None else []
        right_vals = self.right.preorder() if self.right is not None else []
        return [self.value] + left_vals + right_vals

    def inorder(self):
        left_vals = self.left.inorder() if self.left is not None else []
        right_vals = self.right.inorder() if self.right is not None else []
        return left_vals + [self.value] + right_vals

    def postorder(self):
        left_vals = self.left.preorder() if self.left is not None else []
        right_vals = self.right.preorder() if self.right is not None else []
        return left_vals + right_vals + [self.value]


if __name__ == '__main__':
    # Root
    tree = BinaryTree(4)
    
    left = BinaryTree(3)
    left.set_left(BinaryTree(1))
    left.set_right(BinaryTree(20))
    
    right = BinaryTree(7)
    right.set_left(BinaryTree(6))
    right.set_right(BinaryTree(30))
    
    # set root and left child
    tree.set_left(left)
    # set root and right child
    tree.set_right(right)

    print 'Preorder: ', tree.preorder()
    print 'Inorder: ', tree.inorder()
    print 'Postorder: ', tree.postorder()
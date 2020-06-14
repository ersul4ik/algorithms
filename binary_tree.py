
class BinaryTree:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

    def insert(self, element):
        if element < self.data:
            if self.left is None:
                self.left = BinaryTree(element)
            else:
                self.left.insert(element)
        elif element > self.data:
            if self.right is None:
                self.right = BinaryTree(element)
            else:
                self.right.insert(element)


if __name__ == "__main__":
    tree = BinaryTree(22)
    tree.insert(3)
    tree.insert(14)
    tree.insert(33)

    # Tests checking for the correct working of the insert method
    assert tree.data == 22
    assert tree.left.data == 3
    assert tree.left.right.data == 14
    assert tree.left.left == None
    assert tree.right.data == 33
    assert tree.right.left == None
    assert tree.right.right == None






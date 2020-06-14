
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

    def print(self):
        print(self.data)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()


if __name__ == "__main__":
    tree = BinaryTree(22)
    tree.insert(3)
    tree.insert(14)
    tree.insert(33)

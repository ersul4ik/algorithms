from binary_tree import BinaryTree


class Solution:
    _count = 0

    def count_nodes(self, root: BinaryTree) -> int:
        if not root:
            return 0
        self._count += 1
        self.count_nodes(root.left)
        self.count_nodes(root.right)
        return self._count


if __name__ == '__main__':
    tree = BinaryTree(22)
    tree.insert(3)
    tree.insert(14)
    tree.insert(33)

    count_nodes = Solution().count_nodes(tree)
    assert count_nodes == 4

    tree.insert(1)
    count_nodes = Solution().count_nodes(tree)
    assert count_nodes == 5

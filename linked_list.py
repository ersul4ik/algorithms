class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

    def insert(self, element):
        if self.next is None:
            self.next = ListNode(element)
        else:
            self.next.insert(element)

    @classmethod
    def delete_node(cls, node):
        if node is None:
            return None
        if node.next is None:
            raise ValueError('The given node will not be the tail')
        node.value = node.next.value
        node.next = node.next.next


if __name__ == '__main__':
    linked_list = ListNode(4)
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(12)

    assert linked_list.value == 4
    assert linked_list.next.value == 3
    assert linked_list.next.next.value == 2
    assert linked_list.next.next.next.value == 12

    # Cover delete node method with assertions
    ListNode.delete_node(linked_list.next)
    assert linked_list.value == 4
    assert linked_list.next.value == 2

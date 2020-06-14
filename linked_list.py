class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

    def insert(self, element):
        if self.next is None:
            self.next = ListNode(element)
        else:
            self.next.insert(element)


if __name__ == '__main__':
    linked_list = ListNode(4)
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(12)

    assert linked_list.value == 4
    assert linked_list.next.value == 3
    assert linked_list.next.next.value == 2
    assert linked_list.next.next.next.value == 12

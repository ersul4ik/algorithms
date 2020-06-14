from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)
        helper(0, len(s) - 1)


if __name__ == '__main__':
    name = ['r', 'i', 'c', 'h', 'a', 'r', 'd']
    operation = Solution()
    operation.reverse_string(name)

    assert name == ['d', 'r', 'a', 'h', 'c', 'i', 'r']

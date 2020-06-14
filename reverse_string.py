from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)):
            s[i], s[-1 - i] = s[-1 - i], s[i]



if __name__ == '__main__':
    name = ['r', 'i', 'c', 'h', 'a', 'r', 'd']
    operation = Solution()
    operation.reverse_string(name)

    assert name == ['d', 'r', 'a', 'h', 'c', 'i', 'r']

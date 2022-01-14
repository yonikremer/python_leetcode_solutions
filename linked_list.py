from collections import deque
from typing import Union


class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next: Union[LinkedListNode, None] = None

    def __reversed__(self):
        """Returns the reversed Linked List starting from the node self
        accepted by leetcode Runtime: O(n)"""
        stack = deque([])
        curr: LinkedListNode = self
        count = 0
        while curr is not None:
            stack.append(curr.value)
            curr = curr.next
            count += 1
        if count == 0:
            return
        last_node: LinkedListNode = LinkedListNode(value=stack.pop())
        head = last_node
        for _ in range(count - 1):
            next_node = LinkedListNode(value=stack.pop())
            last_node.next = next_node
            last_node = next_node
        self.value = head.value
        self.next = head.next
        return self

    def __str__(self):
        ans = ""
        curr: LinkedListNode = self
        while curr is not None:
            ans += (str(curr.value) + " ")
            curr = curr.next
        return ans

    def last_and_ith_nodes(self, i: int):
        curr: LinkedListNode = self
        try:
            last = None
            for _ in range(i):
                last: LinkedListNode = curr
                curr = curr.next
            return last, curr
        except AttributeError:
            return None

    def cut_and_return_next(self, length: int):
        curr: LinkedListNode = self
        try:
            for _ in range(length):
                curr = curr.next
            next_node = curr.next
            curr.next = None
            return next_node
        except AttributeError:
            pass

    # def get_section(self, start: int, finish: int):
    #     _, new_head = self.last_and_ith_nodes(start)
    #     if new_head is None:
    #         return None
    #     length = finish - start
    #     new_head.cut_and_return_next(length)
    #     return new_head

    def last_node(self):
        curr = self
        while curr.next is not None:
            curr = curr.next
        return curr

    def reverse_between(self, start: int, finish: int):
        """All variables are nodes"""
        if start >= finish:
            return self
        before, section = self.last_and_ith_nodes(start)  # List[start-1], List[start]
        length = finish - start
        next_node = section.cut_and_return_next(length)  # List[finish + 1]
        assert not isinstance(next_node, tuple)
        rev_section = reversed(section)
        assert not isinstance(rev_section, tuple)
        last_rev = rev_section.last_node()
        assert not isinstance(last_rev, tuple)
        before.next = rev_section
        last_rev.next = next_node
        return self

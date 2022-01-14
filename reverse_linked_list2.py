from linked_list import LinkedListNode
from typing import List

if __name__ == "__main__":
    my_list: List[int] = list(map(int, input().strip().split()))
    curr = LinkedListNode(value=my_list[0])
    head = curr
    for i in range(1, len(my_list)):
        curr.next = LinkedListNode(value=my_list[i])
        curr = curr.next
    start = int(input())
    finish = int(input())
    rev = head.reverse_between(start, finish)
    print(rev)

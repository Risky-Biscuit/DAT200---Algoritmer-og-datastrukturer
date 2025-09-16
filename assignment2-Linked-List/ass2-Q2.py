"""
Q2. Write a program that removes the duplicated elements in a circular doubly linked list.

for example: you have populated the linked list with these elements and want to remove the duplicated ones
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None
    prev: Optional["Node"] = None


def from_list_circular(values: list[int]) -> Optional[Node]:
    if not values:
        return None

    head = Node(values[0])
    prev = head

    for x in values[1:]:
        node = Node(x)
        prev.next = node  # forward link: old tail -> new node
        node.prev = prev  # backward link: new node -> old tail
        prev = node  # move tail bookmark forward

    prev.next = head  # last -> first
    head.prev = prev  # first -> last

    return head


def remove_duplicates(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None
    if head.next is head:
        return head
    seen = {head.val}
    p = head.next

    while p is not head:
        if p.val in seen:
            nxt = p.next  # 1) place a checkpoint/bookmark at the next value
            p.prev.next = p.next  # 2) unlink p forward
            p.next.prev = p.prev  # 3) unlink p backward
            p = nxt  # 4) "restart at checkpoint"
        else:
            seen.add(p.val)
            p = p.next  # advance normally

    return head


if __name__ == "__main__":
    head = from_list_circular([4, 4, 6, 8, 8, 12, 12, 4])
    remove_duplicates(head)

    # Traverse one lap to verify the result:
    p = head
    out = [str(p.val)]
    p = p.next
    while p is not head:
        out.append(str(p.val))
        p = p.next
    print(" -> ".join(out))

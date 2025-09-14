"""
Q1. Write a program that finds and prints the minimum and maximum values in a singly linked list.

>> So you need to create a singly linked list and populate it with some data.
>> Write a function to find the min and max values.
"""

from __future__ import (
    annotations,
)  # Let's me use Node as a type hint before it is fully defined
from dataclasses import dataclass  # No need for __init__ and such
from typing import Optional  # Basically "Node or None", in this case


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None


def from_list(values: list[int]) -> Optional[Node]:
    # Return head of singly linked list
    head = None
    tail = None
    for x in values:
        node = Node(x)
        if head is None:  # first element
            head = node
            tail = node
        else:  # attach new node at the end
            tail.next = node
            tail = node
    return head


def min_max(head: Node) -> tuple[int, int]:
    if head is None:
        raise ValueError("List is empty.")

    min_val = head.val
    max_val = head.val

    p = head.next
    while p:
        if p.val < min_val:
            min_val = p.val
        if p.val > max_val:
            max_val = p.val
        p = p.next
    return (min_val, max_val)


if __name__ == "__main__":
    head = from_list([6, 1, 2, 3, 4, 5, 7, 9, 120, -3])

    # print(min_max(head))

    mn, mx = min_max(head)
    print("min", mn)
    print("max", mx)

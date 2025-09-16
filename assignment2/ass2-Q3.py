"""
Q3. Write a program that reads the K value as an input and swaps the first K nodes with the last K nodes in a doubly linked list.

for example: 1 and 8 have been swapped, 2 and 7 have been swapped.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None
    prev: Optional["Node"] = None


def from_list(values: list[int]) -> Optional[Node]:
    if not values:
        return None

    head = Node(values[0])
    prev = head

    for x in values[1:]:
        node = Node(x)
        prev.next = node  # link forward
        node.prev = prev  # link backward
        prev = node  # slide the tail marker forward

    return head


def tail_and_len(head) -> tuple[Optional[Node], int]:
    if head is None:
        return (None, 0)
    n = 1
    p = head
    while p.next is not None:
        p = p.next
        n += 1
    return (p, n)  # p is the tail, n is the length


def swap_first_last_k(head: Optional[Node], k: int) -> Optional[Node]:
    # trivial/invalid cases
    if head is None:
        return None
    if k <= 0:
        return head

    tail, n = tail_and_len(head)
    if n == 0 or tail is None:
        return head

    # if K is larger than half the list, only the first half can be swapped pairwise
    k_eff = min(k, n // 2)

    # pointers from each end
    left = head
    right = tail

    # do k_eff pairwise swaps of the values
    for _ in range(k_eff):
        left.val, right.val = right.val, left.val
        left = left.next
        right = right.prev

    return head


while True:
    try:
        k = int(input("What do you want k to be? "))
        break
    except ValueError:
        print("k has to be an integer.")


if __name__ == "__main__":
    head = from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    swap_first_last_k(head, k)

    # print to verify
    p = head
    out = []
    while p:
        out.append(str(p.val))
        p = p.next
    print(" ".join(out))

# Assignment 2 - Linked-List

"""
Criteria:

It can be done in a group of three students (recommended)
You need to present it during the lab sessions and get it approved by the Student assistants.
You need to have all questions ready while attending the lab
The algorithms should work for any possible inputs and conditions
At least 3 questions should work in order to get it approved.


////////////////////////////////////////////////

Q1. Write a program that finds and prints the minimum and maximum values in a singly linked list.

>> So you need to create a singly linked list and populate it with some data.
>> Write a function to find the min and max values.
for example:

ov2.JPG

/////////////////////////////////////////////////////////

Q2. Write a program that removes the duplicated elements in a circular doubly linked list.

for example: you have populated the linked list with these elements and want to remove the duplicated ones...

ov1.JPG

//////////////////////////////////////////////////////////

Q3. Write a program that reads the K value as an input and swaps the first K nodes with the last K nodes in a doubly linked list.

for example: 1 and 8 have been swapped, 2 and 7 have been swapped.

ov3.JPG

////////////////////////////////////////

Q4: Build a to-do list application using a linked list to manage tasks.

4.1: Include features like adding, deleting, and displaying tasks.
4.2: Expanding the to-do list application to include task priorities, due dates, and the ability to mark tasks as completed can make it more versatile and useful.
Hint: The Task class includes description, priority, due_date, and completed attributes.
/////////////////////////////////////////
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None


def from_list(values: list[int]) -> Optional[Node]:
    # Return head of singly linked list built from values in order
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

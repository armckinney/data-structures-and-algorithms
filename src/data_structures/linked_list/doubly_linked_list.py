from __future__ import annotations

from typing import Any, Optional

from data_structures.core import LinearStructure

from .doubly_linked_list_node import DoublyLinkedListNode


# TODO: all
class DoublyLinkedList(LinearStructure):
    head: Optional[DoublyLinkedListNode] = None
    tail: Optional[DoublyLinkedListNode] = None

    @property
    def empty(self) -> bool:
        return all([self.head is None, self.tail is None])

    @classmethod
    def from_list(cls, list: list) -> DoublyLinkedList:
        linked_list = DoublyLinkedList()
        for value in list:
            linked_list.append(value)

        return linked_list

    def to_list(self) -> list:
        this_node = self.head
        value_list = []

        while this_node:
            value_list.append(this_node.value)
            this_node = this_node.next

        return value_list

    def append(self, value: Any) -> None:
        # add a value to the tail of the list
        node = DoublyLinkedListNode(value, None)

        if not self.head:
            self.head = node
            self.tail = node

        self.tail.next = node
        self.tail = node

    def prepend(self, value: Any) -> None:
        # add a value to the head of the list
        node = DoublyLinkedListNode(value, self.head)

        if not self.tail:
            self.head = node
            self.tail = node

        self.head = node

    def pop(self, tail: bool = False) -> Optional[Any]:
        # remove the head/tail from the list and return it
        popped: Optional[DoublyLinkedListNode] = None

        # empty list
        if not self.head:
            popped = None

        # pop tail
        elif tail:
            # pop tail
            popped = self.tail
            this_node = self.head

            # set new tail to previous
            while this_node:
                if this_node.next == self.tail:
                    self.tail = this_node
                    self.tail.next = None
                this_node = this_node.next

        # pop head
        else:
            popped = self.head
            self.head = self.head.next

        return popped.value

    def delete(self, value: Any, all_occurences: bool = False) -> None:
        # delete occurence(s) of a value
        previous_node: Optional[DoublyLinkedListNode] = None
        deleted_flag: bool = False
        this_node = self.head

        while this_node:
            # delete node
            if this_node.value == value:
                if this_node == self.head:
                    self.head = this_node.next
                elif this_node == self.tail:
                    self.tail = previous_node
                    previous_node.next = None
                else:
                    previous_node.next = this_node.next
                deleted_flag = True
            else:
                # only reassign previous node if not deleting
                previous_node = this_node

            if not all_occurences and deleted_flag:
                break

            this_node = this_node.next

    def reverse(self) -> None:
        # reverse the list in place
        this_node = self.head
        previous_node: Optional[DoublyLinkedListNode] = None
        next_node: Optional[DoublyLinkedListNode] = None

        while this_node:
            # store next node
            next_node = this_node.next

            # set next to previous
            this_node.next = previous_node

            # iterate previous and this node
            previous_node = this_node
            this_node = next_node

        # set head and tail
        self.tail = self.head
        self.head = previous_node

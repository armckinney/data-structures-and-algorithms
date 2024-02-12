from abc import ABC, abstractmethod
from typing import Any, Optional, TypeVar

from data_structures.core import LinearStructure

from .linked_list_node import LinkedListNode

TNode = TypeVar("TNode", bound=LinkedListNode)


class LinkedListMixin(LinearStructure, ABC):
    head: Optional[TNode] = None
    tail: Optional[TNode] = None

    def __init__(self, circular: bool = False) -> None:
        self.is_circular = circular

    @abstractmethod
    def _link(self, node: TNode, next_node: TNode) -> None:
        raise NotImplementedError

    @abstractmethod
    def _get_previous_node(self, node: TNode) -> TNode:
        raise NotImplementedError

    @property
    def empty(self) -> bool:
        return all([self.head is None, self.tail is None])

    @classmethod
    def from_list(cls, list: list) -> LinearStructure:
        linked_list = cls()
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

    def make_circular(self) -> None:
        self.is_circular = True
        self.enforce_circular()

    def enforce_circular(self) -> None:
        if self.is_circular:
            self._link(self.tail, self.head)
        else:
            self.tail.next = None

    def append(self, node: TNode) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self._link(self.tail, node)
            self.tail = node
            self.enforce_circular()

    def prepend(self, node: TNode) -> None:
        # add a value to the head of the list
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self._link(node, self.head)
            self.head = node
            self.enforce_circular()

    def pop(self, tail: bool = False) -> Optional[Any]:
        # remove the head/tail from the list and return it
        popped: Optional[TNode] = None

        # empty list
        if not self.head:
            popped = None

        # pop tail
        elif tail:
            # pop tail
            popped = self.tail

            previous_node: TNode = self._get_previous_node(popped)
            self.tail = previous_node
            self.enforce_circular()

        # pop head
        else:
            popped = self.head
            self.head = self.head.next

        return popped.value

    def delete(self, value: Any, all_occurences: bool = False) -> None:
        # delete occurence(s) of a value
        previous_node: Optional[TNode] = None
        deleted_flag: bool = False
        this_node = self.head

        while this_node:
            # delete node
            if this_node.value == value:
                if this_node == self.head:
                    self.head = this_node.next
                    self.enforce_circular()
                elif this_node == self.tail:
                    self.tail = previous_node
                    self.enforce_circular()
                else:
                    self._link(previous_node, this_node.next)
                deleted_flag = True
            else:
                # only reassign previous node if not deleting
                previous_node = this_node

            if not all_occurences and deleted_flag:
                break

            this_node = this_node.next

    def reverse(self) -> None:
        # reverse the list in place
        previous_node: Optional[TNode] = self.head
        this_node = previous_node.next
        next_node: Optional[TNode] = None

        while this_node:
            # store next node
            next_node = this_node.next

            self._link(this_node, previous_node)

            # iterate previous and this node
            previous_node = this_node
            this_node = next_node

        # set head and tail
        self.tail = self.head
        self.head = previous_node
        self.enforce_circular()

from __future__ import annotations

from typing import Any, Optional

from data_structures.core import LinearStructure
from data_structures.linked_list import LinkedList


class Stack(LinearStructure):
    def __init__(self) -> None:
        self._linked_list = LinkedList(circular=False)

    @classmethod
    def from_list(cls, list: list) -> Stack:
        stack = cls()
        linked_list = LinkedList()
        for value in list:
            linked_list.prepend(value)
        stack._linked_list = linked_list
        return stack

    def to_list(self) -> list:
        return self._linked_list.to_list()

    @property
    def empty(self) -> bool:
        return self._linked_list.empty

    def push(self, value: Any) -> None:
        self._linked_list.prepend(value)

    def pop(self) -> Optional[Any]:
        return self._linked_list.pop(tail=False)

    def peek(self) -> Optional[Any]:
        if not self._linked_list.head:
            return None
        return self._linked_list.head.value

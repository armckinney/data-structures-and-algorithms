from __future__ import annotations

from typing import Any, Optional

from data_structures.core import LinearStructure
from data_structures.linked_list import LinkedList


class Queue(LinearStructure):
    def __init__(self) -> None:
        self._linked_list = LinkedList(circular=False)

    @classmethod
    def from_list(cls, list: list) -> Queue:
        queue = cls()
        queue._linked_list = LinkedList.from_list(list)
        return queue

    def to_list(self) -> list:
        return self._linked_list.to_list()

    @property
    def empty(self) -> bool:
        return self._linked_list.empty

    def enqueue(self, value: Any) -> None:
        self._linked_list.append(value)

    def dequeue(self) -> Optional[Any]:
        return self._linked_list.pop(tail=False)

    def peek(self) -> Optional[Any]:
        if not self._linked_list.head:
            return None
        return self._linked_list.head.value

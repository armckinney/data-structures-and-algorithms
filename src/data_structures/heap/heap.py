from __future__ import annotations

from typing import Any, Callable, Optional, cast

from ..core.linear_structure import LinearStructure


class Heap(LinearStructure):
    def __init__(self, comparator: Optional[Callable[[Any, Any], bool]] = None):
        self._items: list[Any] = []
        # Default to min-heap behavior: a < b
        self._comparator = comparator if comparator else lambda a, b: a < b

    @classmethod
    def from_list(cls, list: list) -> Heap:
        heap = cls()
        for item in list:
            heap.push(item)
        return heap

    def to_list(self) -> list:
        return self._items.copy()

    def push(self, value: Any) -> None:
        self._items.append(value)
        self._heapify_up(len(self._items) - 1)

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return None
        
        if len(self._items) == 1:
            return self._items.pop()

        root = self._items[0]
        self._items[0] = self._items.pop()
        self._heapify_down(0)
        return root

    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def _heapify_up(self, index: int) -> None:
        parent_index = (index - 1) // 2
        if index > 0 and self._comparator(self._items[index], self._items[parent_index]):
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index: int) -> None:
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self._items) and self._comparator(self._items[left_child], self._items[smallest]):
            smallest = left_child

        if right_child < len(self._items) and self._comparator(self._items[right_child], self._items[smallest]):
            smallest = right_child

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i: int, j: int) -> None:
        self._items[i], self._items[j] = self._items[j], self._items[i]

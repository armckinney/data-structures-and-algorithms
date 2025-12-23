from __future__ import annotations

from typing import Any, Optional, cast

from .linked_list_mixin import LinkedListMixin
from .linked_list_node import LinkedListNode


class LinkedList(LinkedListMixin):
    head: Optional[LinkedListNode] = None
    tail: Optional[LinkedListNode] = None

    @classmethod
    def from_list(cls, list: list) -> LinkedList:
        return cast(LinkedList, super().from_list(list))

    def _link(self, node: Optional[LinkedListNode], next_node: Optional[LinkedListNode]) -> None:
        assert isinstance(node, LinkedListNode)
        assert isinstance(next_node, LinkedListNode)

        node.next = next_node

    def _get_previous_node(self, node: LinkedListNode) -> Optional[LinkedListNode]:
        this_node: Optional[LinkedListNode] = self.head
        while this_node:
            if this_node.next == node:
                return this_node
            this_node = this_node.next

        return this_node

    def append(self, value: Any) -> None:
        # add a value to the tail of the list
        node = LinkedListNode(value, None)
        super().append(node)

    def prepend(self, value: Any) -> None:
        # add a value to the head of the list
        node = LinkedListNode(value, self.head)
        super().prepend(node)

from __future__ import annotations

from typing import Any, Optional

from .linked_list_mixin import LinkedListMixin, TNode
from .linked_list_node import LinkedListNode


class LinkedList(LinkedListMixin):
    head: Optional[LinkedListNode] = None
    tail: Optional[LinkedListNode] = None

    @classmethod
    def from_list(cls, list: list) -> LinkedList:
        return super().from_list(list)

    def _link(self, node: TNode, next_node: TNode) -> TNode:
        assert isinstance(node, LinkedListNode)
        assert isinstance(next_node, LinkedListNode)

        node.next = next_node

    def _get_previous_node(self, node: TNode) -> None:
        this_node = self.head
        while this_node:
            if this_node.next == node:
                return this_node
            this_node = this_node.next

    def append(self, value: Any) -> None:
        # add a value to the tail of the list
        node = LinkedListNode(value, None)
        super().append(node)

    def prepend(self, value: Any) -> None:
        # add a value to the head of the list
        node = LinkedListNode(value, self.head)
        super().prepend(node)

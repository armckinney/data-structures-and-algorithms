from __future__ import annotations

from typing import Any, Optional

from .doubly_linked_list_node import DoublyLinkedListNode
from .linked_list_mixin import LinkedListMixin, TNode


class DoublyLinkedList(LinkedListMixin):
    head: Optional[DoublyLinkedListNode] = None
    tail: Optional[DoublyLinkedListNode] = None

    @classmethod
    def from_list(cls, list: list) -> DoublyLinkedList:
        return super().from_list(list)

    def _link(self, node: TNode, next_node: TNode) -> None:
        assert isinstance(node, DoublyLinkedListNode)
        assert isinstance(next_node, DoublyLinkedListNode)

        node.next = next_node
        next_node.previous = node

    def _get_previous_node(self, node: TNode) -> TNode:
        assert isinstance(node, DoublyLinkedListNode)
        return node.previous

    def append(self, value: Any) -> None:
        # add a value to the tail of the list
        node = DoublyLinkedListNode(value, None, self.tail)
        super().append(node)

    def prepend(self, value: Any) -> None:
        # add a value to the head of the list
        node = DoublyLinkedListNode(value, self.head, None)
        super().prepend(node)

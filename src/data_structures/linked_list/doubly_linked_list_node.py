from __future__ import annotations

from dataclasses import dataclass

from data_structures.core import Node


@dataclass
class DoublyLinkedListNode(Node):
    next: DoublyLinkedListNode
    previous: DoublyLinkedListNode

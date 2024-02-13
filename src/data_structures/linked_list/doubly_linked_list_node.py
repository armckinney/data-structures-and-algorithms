from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .linked_list_node import LinkedListNode


@dataclass
class DoublyLinkedListNode(LinkedListNode):
    previous: Optional[DoublyLinkedListNode]
    next: Optional[DoublyLinkedListNode]

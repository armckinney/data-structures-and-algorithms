from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from data_structures.core import Node


@dataclass
class DoublyLinkedListNode(Node):
    next: Optional[DoublyLinkedListNode]
    previous: Optional[DoublyLinkedListNode]

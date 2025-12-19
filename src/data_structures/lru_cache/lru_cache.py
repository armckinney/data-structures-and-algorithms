from __future__ import annotations

import json
from typing import Any, Dict, Optional

from data_structures.core import MappedStructure
from data_structures.linked_list.doubly_linked_list_node import DoublyLinkedListNode


class LRUCache(MappedStructure):
    """
    Implementation of the LRU (Least Recently Used) Cache
    based on the HashMap and Doubly Linked List data-structures.

    Current implementation allows to have fast O(1) (in average) read and write operations.

    At any moment in time the LRU Cache holds not more that "capacity" number of items in it.
    """

    def __init__(self, capacity: int) -> None:
        """
        Creates a cache instance of a specific capacity.
        """
        self.capacity = capacity
        # How many items to store in cache at max.
        self.nodes_map: Dict[str, DoublyLinkedListNode] = {}
        # The quick links to each linked list node in cache.
        self.size = 0
        # The number of items that is currently stored in the cache.
        self.head = DoublyLinkedListNode(None, None, None)
        # The Head (first) linked list node.
        self.tail = DoublyLinkedListNode(None, None, None)
        # The Tail (last) linked list node.

    @classmethod
    def from_dict(cls, dict: dict) -> LRUCache:
        """
        Creates an LRUCache from a dictionary.
        Note: The order in the dict will be the initial LRU order.
        """
        cache = cls(len(dict) or 1)
        for key, value in dict.items():
            cache.set(str(key), value)
        return cache

    def to_dict(self) -> dict:
        """
        Returns the cache contents as a dictionary (LRU to MRU order).
        """
        result = {}
        current = self.head.next
        while current and current != self.tail:
            # node.value stores [key, val]
            key, val = current.value
            result[key] = val
            current = current.next
        return result

    def to_string(self) -> str:
        """
        Returns a JSON string representation of the cache.
        """
        return json.dumps(self.to_dict())

    def get(self, key: str) -> Any:
        """
        Returns the cached value by its key.
        Time complexity: O(1) in average.
        """
        if key not in self.nodes_map:
            return None

        node = self.nodes_map[key]
        self.promote(node)
        return node.value[1]

    def set(self, key: str, val: Any) -> None:
        """
        Sets the value to cache by its key.
        Time complexity: O(1) in average.
        """
        if key in self.nodes_map:
            node = self.nodes_map[key]
            node.value = [key, val]
            self.promote(node)
        else:
            node = DoublyLinkedListNode([key, val], None, None)
            self.append(node)

    def promote(self, node: DoublyLinkedListNode) -> None:
        """
        Promotes the node to the end of the linked list.
        It means that the node is most frequently used.
        It also reduces the chance for such node to get evicted from cache.
        """
        self.evict(node)
        self.append(node)

    def append(self, node: DoublyLinkedListNode) -> None:
        """
        Appends a new node to the end of the cache linked list.
        """
        if node.value is not None:
            key = node.value[0]
            self.nodes_map[key] = node

        if not self.head.next:
            # First node to append.
            self.head.next = node
            self.tail.previous = node
            node.previous = self.head
            node.next = self.tail
        else:
            # Append to an existing tail.
            old_tail = self.tail.previous
            if old_tail:
                old_tail.next = node
            node.previous = old_tail
            node.next = self.tail
            self.tail.previous = node

        self.size += 1

        if self.size > self.capacity:
            if self.head.next:
                self.evict(self.head.next)

    def evict(self, node: DoublyLinkedListNode) -> None:
        """
        Evicts (removes) the node from cache linked list.
        """
        if node.value is not None:
            key = node.value[0]
            if key in self.nodes_map:
                del self.nodes_map[key]
                self.size -= 1

        prev_node = node.previous
        next_node = node.next

        # If one and only node (between head/tail dummies).
        if prev_node == self.head and next_node == self.tail:
            self.head.next = None
            self.tail.previous = None
            self.size = 0
            return

        # If this is a Head node (first after dummy head).
        if prev_node == self.head:
            if next_node:
                next_node.previous = self.head
            self.head.next = next_node
            return

        # If this is a Tail node (last before dummy tail).
        if next_node == self.tail:
            if prev_node:
                prev_node.next = self.tail
            self.tail.previous = prev_node
            return

        # If the node is in the middle.
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.previous = prev_node

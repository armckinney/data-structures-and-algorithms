from __future__ import annotations

import hashlib
from typing import Any

from ..core.mapped_structure import MappedStructure


class BloomFilter(MappedStructure):
    def __init__(self, size: int = 100, num_hashes: int = 3):
        """
        Initialize a Bloom Filter with a given size and number of hash functions.

        Args:
            size: The size of the bit array (m).
            num_hashes: The number of hash functions to use (k).
        """
        if size <= 0:
            raise ValueError("Size must be positive")
        if num_hashes <= 0:
            raise ValueError("Number of hashes must be positive")

        self._size = size
        self._num_hashes = num_hashes
        self._bit_array = 0  # efficient bit array using python integer

    @property
    def size(self) -> int:
        return self._size

    @property
    def num_hashes(self) -> int:
        return self._num_hashes

    def add(self, item: Any) -> None:
        """
        Add an item to the Bloom Filter.
        """
        item_str = str(item)
        for i in range(self._num_hashes):
            digest = self._hash(item_str, i)
            self._bit_array |= 1 << digest

    def check(self, item: Any) -> bool:
        """
        Check if an item is possibly in the Bloom Filter.
        Return True if the item might be in the set, False if it is definitely not.
        """
        item_str = str(item)
        for i in range(self._num_hashes):
            digest = self._hash(item_str, i)
            if not (self._bit_array & (1 << digest)):
                return False
        return True

    def _hash(self, item: str, i: int) -> int:
        """
        Double hashing to simulate k hash functions.
        h_i(x) = (h1(x) + i * h2(x)) % m
        """
        encoded = item.encode("utf-8")
        h1 = int(hashlib.md5(encoded).hexdigest(), 16)
        h2 = int(hashlib.sha1(encoded).hexdigest(), 16)
        return (h1 + i * h2) % self._size

    def to_dict(self) -> dict:
        return {"size": self._size, "num_hashes": self._num_hashes, "bit_array": self._bit_array}

    @classmethod
    def from_dict(cls, data: dict) -> BloomFilter:
        bf = cls(size=data["size"], num_hashes=data["num_hashes"])
        bf._bit_array = data["bit_array"]
        return bf

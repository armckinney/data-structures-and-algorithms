from __future__ import annotations

from typing import Any

from data_structures.core import MappedStructure
from data_structures.linked_list import LinkedList

from .hash_object import HashObject


class HashTable(MappedStructure):

    def __init__(self, size: int = 32) -> None:
        self.size = size

        # quick key tracking
        self.keys: dict[Any, int] = {}

        # create empty LinkedList buckets
        self._buckets = [LinkedList(circular=False) for _ in range(size)]

    @classmethod
    def from_dict(cls, dict: dict, size: int = 32) -> HashTable:
        hash_table = HashTable(size)
        for key, value in dict.items():
            hash_table.set(key, value)

        return hash_table

    def to_dict(self) -> dict:
        keys_dict = self.keys.copy()

        for bucket in self._buckets:
            bucket_list: list[HashObject] = bucket.to_list()
            bucket_map = {ho.key: ho.value for ho in bucket_list}
            keys_dict.update(bucket_map)

        return keys_dict

    def _hash(self, key: Any) -> int:
        hash_value = abs(hash(key))
        return hash_value % self.size

    def set(self, key: Any, value: Any) -> None:
        key_hash = self._hash(key)
        self.keys[key] = key_hash
        target_bucket = self._buckets[key_hash]
        hashobj: HashObject = target_bucket.find(callback=lambda x: x.key == key)

        if not hashobj:
            target_bucket.append(HashObject(key, value))
        else:
            hashobj.value = value

    def get(self, key: Any) -> Any:
        key_hash = self._hash(key)
        target_bucket = self._buckets[key_hash]
        hashobj: HashObject = target_bucket.find(callback=lambda x: x.key == key)

        return hashobj.value

    def pop(self, key: Any) -> Any:
        key_hash = self._hash(key)
        self.keys.pop(key)
        target_bucket = self._buckets[key_hash]
        hashobj: HashObject = target_bucket.find(callback=lambda x: x.key == key)

        if hashobj:
            target_bucket.delete(hashobj)

        return hashobj.value

    def delete(self, key: Any) -> None:
        self.pop(key)

    def has(self, key: Any) -> bool:
        return key in self.get_keys()

    def get_keys(self) -> list[Any]:
        return list(self.keys.keys())

    def get_values(self) -> list[Any]:
        values = []

        for bucket in self._buckets:
            bucket_list: list[HashObject] = bucket.to_list()
            values.extend([ho.value for ho in bucket_list])

        return values

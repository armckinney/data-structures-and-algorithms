from __future__ import annotations

import json
from abc import ABC, abstractmethod

from .data_structure import DataStructure


class MappedStructure(DataStructure, ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, dict: dict) -> MappedStructure:
        raise NotImplementedError

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    def to_string(self) -> str:
        as_dict = self.to_dict()
        return json.dumps(as_dict)

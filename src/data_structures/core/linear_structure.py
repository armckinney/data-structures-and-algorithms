from __future__ import annotations

from abc import ABC, abstractmethod

from .data_structure import DataStructure


class LinearStructure(DataStructure, ABC):

    @classmethod
    @abstractmethod
    def from_list(cls, list: list) -> LinearStructure:
        raise NotImplementedError

    @abstractmethod
    def to_list(self) -> list:
        raise NotImplementedError

    def to_string(self) -> str:
        """
        Universal / Non-optimized conversion to string.
        """
        string_list = [str(i) for i in self.to_list()]
        return "".join(string_list)

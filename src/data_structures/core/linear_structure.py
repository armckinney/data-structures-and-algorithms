from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TStructure = TypeVar("TStructure")


class LinearStructure(ABC, Generic[TStructure]):

    @classmethod
    @abstractmethod
    def from_list(cls) -> TStructure:
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

from abc import ABC, abstractclassmethod, abstractmethod
from typing import Any, Generic, TypeVar

TStructure = TypeVar("TStructure")


class LinearStructure(ABC, Generic[TStructure]):

    @abstractclassmethod
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

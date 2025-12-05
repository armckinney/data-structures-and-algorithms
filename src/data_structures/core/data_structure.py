from abc import ABC, abstractmethod


class DataStructure(ABC):
    @abstractmethod
    def to_string(self) -> str:
        raise NotImplementedError

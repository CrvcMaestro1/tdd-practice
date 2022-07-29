from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def get_password(self, username: str) -> str:
        pass

from typing import Protocol


class IPasswordHasher(Protocol):
    def hash(self, password: str) -> str:
        raise NotImplementedError

    def verify(self, password: str, h_password: str) -> bool:
        raise NotImplementedError
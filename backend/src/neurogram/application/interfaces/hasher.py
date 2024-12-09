from typing import Protocol


class PasswordHasher(Protocol):
    def hash(self, password: str) -> str:
        raise NotImplementedError

    def verify(self, password: str, h_password: str) -> bool:
        raise NotImplementedError
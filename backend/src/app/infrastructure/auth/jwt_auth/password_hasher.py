import bcrypt
from app.application.interfaces.hasher import IPasswordHasher


class PasswordHasher(IPasswordHasher):
    def hash(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def verify(self, password: str, h_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), h_password.encode("utf-8"))

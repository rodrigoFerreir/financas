from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def generate_hash_password(password):
    return pwd_context.hash(password)


def verify_hash_password(password, hash_password):
    return pwd_context.verify(password, hash_password)

import hashlib
import base64, os


def generate_password_hash(password):

    password = password.encode('utf-8')

    salt = base64.b64encode(os.urandom(32))

    salting_hash256 = hashlib.sha256(salt + password).hexdigest()
    for _ in range(1000):
        salting_hash256 = hashlib.sha256(bytes(salting_hash256, 'utf-8')).hexdigest()
    return salting_hash256

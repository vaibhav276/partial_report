import random
from passlib.hash import sha256_crypt

def encrypt_password(raw_password):
    return sha256_crypt.encrypt(raw_password)

def verify_password(raw_password, hsh):
    return sha256_crypt.verify(raw_password, hsh)

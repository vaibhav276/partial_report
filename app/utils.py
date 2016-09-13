import random
from passlib.hash import sha256_crypt

def encrypt_password(raw_password):
    return sha256_crypt.encrypt(raw_password)

def verify_password(raw_password, hsh):
    return sha256_crypt.verify(raw_password, hsh)

def count_matches(matrix, size, cue_row, response):
    start_pos = size * (cue_row -1)
    end_pos = start_pos + size
    chunk = matrix[start_pos:end_pos]
    match_chars = 0
    for i, char in enumerate(chunk):
        if response[i] == char:
            match_chars = match_chars + 1

    return match_chars

import hashlib


def to_md5_hex(content):
    return hashlib.md5(content.encode()).hexdigest()
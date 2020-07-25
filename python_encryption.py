# Here we encrypt a str using a one-time pad, A one-time pad is a way of encrypting a piece of data by combining it with meaningless
# random dummy data in such a way that the original cannot be reconstituted without
# access to both the product and the dummy data


from secrets import token_bytes
from typing import Tuple


# This function creates an int filled with length random bytes.
def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)

    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")


# This function encodes the str passeed into it and returns a key pair (dummy and encrypted)
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy   # XOR (exlusive or)
    return dummy, encrypted


# Getting the encoded str back
def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2    # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1, key2)
    print(result)

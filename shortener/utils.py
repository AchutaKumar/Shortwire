ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE = len(ALPHABET)
MIN_LENGTH = 5


def encode_base62(num: int) -> str:
    if num == 0:
        return "A" + "0" * (MIN_LENGTH - 1)

    digits = []
    while num:
        num, rem = divmod(num, BASE)
        digits.append(ALPHABET[rem])

    code = "".join(reversed(digits))
    if len(code) < MIN_LENGTH:
        code = code.rjust(MIN_LENGTH, ALPHABET[0])

    if len(code) == MIN_LENGTH and code[0].isdigit():
        code = "A" + code[1:]

    return code
from random import choice
from sys import argv


def cipher(password: str, cipher_keywords: list):
    ciphered:str = ""

    for char in password:
        ciphered += char + choice(cipher_keywords)

    return ciphered


def main(arguments: list):
    args = arguments.copy()
    words = []

    for i in range(1, len(args)):
        args[i] = args[i].split("=")[1].strip()

    with open(args[1], "r") as readfile:
        for line in readfile:
            words += [line.strip()]

    with open(args[2], "w") as writefile:
        writefile.write(cipher(args[3], words))


main(argv)

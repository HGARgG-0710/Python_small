from sys import argv


def main(arguments: list):
    for arg in arguments:
        arg = arg.split("=")[1]

    with open(arg[0]) as readfile:
        input_words = readfile.readlines()

    with open(arg[1], "w") as writefile:
        writefile.write(decipher(arg[2], input_words))


if __name__ == "__main__":
    main(argv)

# TODO Finish the deciphering function.
def decipher(password: str, input_words: list):
    deciphered = password
    curr_substr = ""

    index = 1
    while index < len(password):
        # ! Read the sequance of characters from password and
        # ! check whether it belongs to input_words or not.
        # ! If so, then skip it (delete from it's original
        # ! indexes from deciphered string).
        pass

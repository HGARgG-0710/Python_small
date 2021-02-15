letterString = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
alphabet = list(letterString)
bigLetters = alphabet[::2]
smallLetters = alphabet[1::2]
backwards = alphabet[::-1]

print("English alphabet:", "|", " | ".join(alphabet), "|",  "\n")
print("Capital letters:", "|", " | ".join(bigLetters), "|",  "\n")
print("Small letters:", "|", " | ".join(smallLetters), "|", "\n")
print("Alphabet backwards:", "|", " | ".join(backwards), "|", "\n\n")

print("Alphabet length:", len(alphabet), "\n")

values = input("Now enter three values: starting point of fragment of alphabet(minimum is 1), ending point of it and step(for how many shall the number be increased every iteration): \n").split(" ")
print("\n")
print("Output:", "|", " | ".join(alphabet[int(values[0]) - 1: int(values[1]) - 1: int(values[2])]), "|")

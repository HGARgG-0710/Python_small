import random

def generate(length = 8):
    allowed_items = [
        "a", "b", "c", "d", "e",
        "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o",
        "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y",
        "z", "0", "1", "2", "3",
        "4", "5", "6", "7", "8",
        "9", "#", "!", "_", "-",
        "$"
    ]

    random_str = ""
    
    for i in range(0, 26):
        allowed_items += [allowed_items[i].upper()]

    for i in range(0, length + 1):
        random_str += random.choice(allowed_items) 

    return random_str

length = int(input("Please, input the password length: "))
password = generate(length)

print(password)

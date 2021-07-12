from math import sqrt
from sys import argv


def errApproxSqrt(number):
    nearest_smallest = find_nearest_square(number)
    nearest_biggest = find_nearest_square(number, False)

    result = sqrt(nearest_smallest) + (number - nearest_smallest) / \
        (nearest_biggest - nearest_smallest)

    return result - sqrt(number)


def find_nearest_square(number: int, is_smallest: bool = True):
    r = range(number, 0, -1) if is_smallest else range(number, 2 * number + 1)
    for num in r:
        if float.is_integer(sqrt(num)):
            return num


def eToTen(to_format: str):
    for char in to_format:
        if char == "e":
            return to_format[:to_format.index(char) - 1] + " * (10 ^ " + to_format[to_format.index(char) + 1:] + ")"

    return to_format

last = 0

try: 
    last = int(argv[1]) + 1
except ValueError: 
    print("Error! Passed argument could not be converted to number. ")
except IndexError: 
    print("Not provided any argument at all!")

numbers = []
differences = []

for i in range(0, last):
    if float.is_integer(sqrt(i)):
        continue
    numbers.append(i)
    differences.append(errApproxSqrt(i))

with open("output.txt", "w+") as writefile:
    writefile.write(
        "| a                   | q                                  |\n|_____________________|____________________________________|\n")
    for number in numbers:
        formatted = eToTen(str(-(differences[numbers.index(number)])))
        converted = str(number)
        writefile.write("| " + converted +
                        (" " * (19 - len(converted)) + " | " + formatted +
                         (" " * (34 - len(formatted))) + " |\n"))

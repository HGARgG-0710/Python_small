def isLetter(char):
    return char in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"


input_file = "data.txt"
output_file = "output.txt"

string = ""
result = ""

with open(input_file, "r") as input_file:
    string = input_file.readline().strip()

curr_letter = ""
curr_num = ""
index = 0
chars = list(string)

for char in chars:
    if isLetter(char):
        if index > 0:
            result += curr_letter * int(curr_num)
        curr_letter = char
        curr_num = ""
    else:
        curr_num += char
        if index == len(chars) - 1:
            result += curr_letter * int(curr_num)
    index += 1

with open(output_file, "w") as out:
    out.write(result)

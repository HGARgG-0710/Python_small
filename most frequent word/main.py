filenames = input("Input two filenames divided by space. They shall be used as an input and an output files: ").split()
input_str = ""

with open(filenames[0], "r") as input_file, open(filenames[1], "w") as output_file:
    for line in input_file:
        line = line.strip()
        input_str += line

    data = input_str.split(" ")

    most_frequent_word = ""
    times_found = 0

    for word in data:
        found_curr = input_str.lower().split(" ").count(word.lower())
        if found_curr > times_found:
            times_found = found_curr
            most_frequent_word = word

    output_file.write(most_frequent_word + " " + str(times_found))

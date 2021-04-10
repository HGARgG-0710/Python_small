def arr_sum(arr):
    result = 0
    for item in arr:
        result += item
    return result


def dict_values_average(dictionary):
    total_sum = 0
    answers = []
    for value in dictionary.values():
        total_sum = arr_sum(value)
        answers += [total_sum / len(list(dictionary.values())[0])]
    return answers


filenames = input(
    "Input two filenames divided by space. They shall be used as an input and an output files: ").split(" ")

with open(filenames[0], "r", encoding="utf-8") as input_file, open(filenames[1], "w", encoding="utf-8") as output_file:
    data = [line.strip().split(";") for line in input_file]
    students = {}
    averages_subjects = []

    for line in data:
        students.update({line[0]: [int(mark) for mark in line[1:]]})

    output_file.write("\n".join([str(round(line, 9)) for line in dict_values_average(students)]))

    for num in range(len(list(students.values())[0])):
        temp = []
        for key in students:
            temp += [students[key][num]]
        averages_subjects += [round(arr_sum(temp) / len(temp), 9)]

    output_file.write("\n" + " ".join([str(average) for average in averages_subjects]))

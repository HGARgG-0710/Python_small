import matplotlib.pyplot as pyplot
from math import sqrt
from sys import argv, exit


# Approximation function. 
def approx(number) -> float:
    # Function for calculating the rough approximation. 
    def rough(number) -> float:
        def nearest(number: int, is_smallest: bool) -> int:
            for i in range(number * 2):
                curr_num = number - i if is_smallest else number + i
                if sqrt(curr_num).is_integer():
                    return curr_num

        smallest, biggest = nearest(number, True), nearest(number, False)
        return sqrt(smallest) + (number - smallest) / (biggest - smallest)

    # Function for calculating the correction term. 
    def correction(number) -> float:
        return 1 / (number * 100 * (number // 2))

    # p and z terms 
    rough_approximation = rough(number)
    correction_term = correction(number)

    # Approximation. This the rearranged version.  
    return 0.5 * (rough_approximation + number / rough_approximation - correction_term)

# Error (of my approximation) function. 
def error(number):
    return abs(sqrt(number) - approx(number))


# Data validation step (A bit clumsy).
try:
    start = int(argv[1])
    end = int(argv[2])

    err = False
    message = ""
except ValueError:
    message = "Invalid arguments passed. Expected number, got string. "
    err = True
except IndexError:
    message = "Expected two arguments (start position and end position), got " + str(len(argv) - 1)
    err = True
finally:
    if err:
        print("Error: " + message)
        exit(0)

# List for keeping the results.
err_values = ([], [])

# Iterating...
for i in range(start, end):
    if not (sqrt(i).is_integer()):
        err_values[0].append(i)
        err_values[1].append(error(i))

# And finally...plotting! :)
pyplot.figure(figsize = (1920, 1080))

pyplot.plot(err_values[0], err_values[1], color="lightskyblue")
pyplot.title("My sqrt approximation")

pyplot.xlabel("Numbers")
pyplot.ylabel("Error")

pyplot.grid(True)
pyplot.show()

import matplotlib.pyplot as pyplot
from numpy import cbrt
from sys import argv, exit


# Approximation function.
def approx(number: int) -> float: 
    # Function for calculating the rough approximation of the cube root. 
    def rough(number:int) -> float: 
        def nearest(number:int, is_smallest:bool) -> int: 
            for num in range(1, number * 10): 
                curr_number = number - num if is_smallest else number + num
                if round(curr_number ** (1/3)) ** 3 == curr_number: 
                    return curr_number
        
        smallest = nearest(number, True)
        biggest = nearest(number, False)

        return smallest ** (1 / 3) + (number - smallest)/(biggest - smallest)

    # Correction function. 
    def correction(number: int) -> float: 
        return (1/(9 * number)) 

    # p and z terms 
    rough_approximation = rough(number)
    correction_term = correction(number) 

    return 1/3 * (2 * rough_approximation + (number / (rough_approximation ** 2) - correction_term))


# Error (of my approximation) function. 
def error(number): 
    return abs(cbrt([number])[0] - approx(number))

# Data validation step. 
try: 
    start = int(argv[1])
    end = int(argv[2])

    err = False
except ValueError: 
    err = True
    message = "Invalid values for argument provided: expected numbers, got string. "
except IndexError:  
    err = True
    message = "Too little argument provided. Expected 2, got " + str(len(argv) - 1) 
finally:  
    if err: 
        print("Error: " + message)
        exit(0)

# Arr for storing data. 
err_values = ([], [])

# Iterating...
for i in range(start, end): 
    if round(i ** (1/3)) ** 3 != i: 
        err_values[0].append(i)
        err_values[1].append(error(i))

# And finally...plotting! :)
pyplot.figure(figsize = (1920, 1080))

pyplot.plot(err_values[0], err_values[1], color="brown")
pyplot.title("My cube root approximation")

pyplot.xlabel("Numbers")
pyplot.ylabel("Error")

pyplot.grid(True)
pyplot.show()
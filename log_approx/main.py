"""
! Well, apparently, this log_x approximation is not very good. 
! For myself I would even consider it a failure. 
! I suppose I should (and probably will) rework it, but for now do not know how. 
! I strongly DO NOT recommend to work with it, unless you're ready to take some great lossses in measurements 
! or have no other choice. 

* Any fixes of this approximation would be warmly appreciated, 
* for it is absolutely terrible and is definitely not acceptable. 
* Its problem lie in the complexity of the issue of finding such a formula. 
* For some base values it works relatively alright(4, say) but for the others, the error just blows up at some point. 
* (Just try the "1 1000 3" input and you'll understand what i mean.

Written by: HGARgG-0710, Igor Kuznetsov
"""

from matplotlib import pyplot
from sys import argv, exit
from math import log

def approx(number: int, base: int) -> float:
    def rough(number: int, base: int) -> float: 
        def smaller(number: int, base: int): 
            if number < base:  
                return number 

            final = base
            for num in range(number - 1, base, -1): 
                if log(number / num, base).is_integer(): 
                    return num
                if log(num, base).is_integer():
                    final = num
                    break
            
            # in case the b(a) term is rational, but not integral. 
            return number / final 

        def larger(number: int, base: int):   
            for num in range(number, number * base): 
                if base ** round(log(num, base)) == num: 
                    return num


        smallest  = smaller(number, base)
        largest = larger(number, base)

        return log(number / smallest, base) + (number - smallest) / (largest )
    
    rough_approximation: float = rough(number, base)
    return (47/50) * rough_approximation +  (0.1 if number < base * 10 else 0.3)


def err(number: int, base: int) -> float:  
    return abs(log(number, base) - approx(number, base))

try: 
    base, start, end = int(argv[1]), int(argv[2]), int(argv[3])
    is_err = False
except ValueError: 
    error = "One of the passed parameters to the program is invalid. Expected number, got string. "
    is_err = True
except IndexError: 
    error = "There are not enough parameters passed to the program. Expected three, got " + str(len(argv) - 1)
    is_err = True
finally: 
    if is_err: 
        print("Error: " + error) 
        exit(0)

err_values = ([], [])

for num in range(start, end): 
    if not log(num, base).is_integer(): 
        print(num)
        err_values[0].append(num)
        err_values[1].append(err(num, base))

pyplot.plot(err_values[0], err_values[1], color = "lightgreen")
pyplot.title("Logarithm approximation")

pyplot.xlabel("Values")
pyplot.ylabel("Error")

pyplot.grid(True) 
pyplot.show()
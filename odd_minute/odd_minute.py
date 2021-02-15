from datetime import datetime
from time import sleep
from random import randint

odd_mins = []
output = ""
iteration_res = ""
modif = ""

for i in range(60):
    if not(i % 2 == 0):
        odd_mins += [i]

for j in range(10):
    sleep(randint(1, 15))
    
    if datetime.today().minute in odd_mins:
        output = "This minute is odd."
    else:
        output = "This minute isn't odd."
        
    if (j > 0) and not(iteration_res == output):
        modif = "\n"
    else:
        modif = ""
        
    iteration_res = output
    print(modif, output)

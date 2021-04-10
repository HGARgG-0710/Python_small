genome = input()
changedGenome = ""

total = 1
num = 0

for i in genome:
    if(not (num == (len(genome) - 1))):
        if(i == genome[num + 1]):
            total += 1
        else:
            changedGenome += (i + str(total))
            total = 1
        num += 1
    else:
        changedGenome += (i + str(total))

print(changedGenome)

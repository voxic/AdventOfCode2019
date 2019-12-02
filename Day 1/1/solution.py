import math

rawFuel = []
with open('input.txt') as f:
    for mass in f.readlines():
        print(mass)
        rawFuel.append((math.floor(int(mass)/3))-2)

fuelSum = 0
for fuel in rawFuel:
    fuelSum = fuelSum + fuel

print(fuelSum)

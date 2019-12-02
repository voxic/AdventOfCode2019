import math

rawFuel = []
with open('input.txt') as f:
    for mass in f.readlines():
        print(mass)
        totalFuel = 0
        while(int(mass) >= 0):
            mass = ((math.floor(int(mass)/3))-2)
            if(mass >=0):
                totalFuel = totalFuel + mass
                print(mass)

        rawFuel.append(totalFuel)

fuelSum = 0
for fuel in rawFuel:
    fuelSum = fuelSum + fuel

print(fuelSum)

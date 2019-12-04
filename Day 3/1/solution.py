
with open("3.in", "r") as f:
    def followWire():
        loc = [0, 0]

        for move in f.readline().split(","):
            change = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]] # Look at the first char and map that to a change in the tuple 
            for _ in range(int(move[1:])): # Iterate over the number of steps to be taken
                loc[change[0]] += change[1] # Add the change to the location array
                yield tuple(loc) # Return the current value to be added to the visited array

    visited = set(followWire()) #Array of tuples with all visited cords

    intersections = [] # Array to hold all intersections
    for loc in followWire():
        if loc in visited:
            intersections.append(abs(loc[0]) + abs(loc[1]))

print(min(intersections))


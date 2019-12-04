with open("3.in", "r") as f:
    def followWire():
        loc = [0, 0]
        steps = 0

        for move in f.readline().split(","):
            change = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]] # Look at the first char and map that to a change in the tuple 
            for _ in range(int(move[1:])): # Iterate over the number of steps to be taken
                loc[change[0]] += change[1] # Add the change to the location array
                steps = steps + 1 # Add a step
                yield tuple(loc), steps # Return the current value and steps to be added to the visited array

    visited = {} #Array of tuples with all visited cords

    intersections = [] # Array to hold all intersections
    for loc, steps in followWire():
        if loc not in visited:
            visited[loc] = steps

    for loc, steps in followWire():
        if loc in visited:
            intersections.append(steps + visited[loc])
    
    print(min(intersections))
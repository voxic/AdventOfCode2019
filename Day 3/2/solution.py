with open("3.in", "r") as f:
    def followWire():
        loc = [0, 0]
        steps = 0

        for move in f.readline().split(","):
            change = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]]
            for _ in range(int(move[1:])):
                loc[change[0]] += change[1]
                steps = steps + 1
                yield tuple(loc), steps

    visited = {}

    intersections = []
    for loc, steps in followWire():
        if loc not in visited:
            visited[loc] = steps

    for loc, steps in followWire():
        if loc in visited:
            intersections.append(steps + visited[loc])
    
    print(min(intersections))
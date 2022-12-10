from copy import copy


def parser():
    rules = []
    for line in open("input.txt"):
        vals = line.strip().split(" ")
        rules.append([vals[0], int(vals[1])])
    return rules


def part1(inp):
    coordinates = []
    # current_coord_H_prev = [0, 0]
    current_coord_H = [0, 0]
    current_coord_T = [0, 0]
    for direction, number in inp:
        for _ in range(number):
            current_coord_H_prev = copy(current_coord_H)
            match direction:
                case "L":
                    current_coord_H[0] -= 1
                case "R":
                    current_coord_H[0] += 1
                case "U":
                    current_coord_H[1] += 1
                case "D":
                    current_coord_H[1] -= 1

            if abs(current_coord_H[0] - current_coord_T[0]) > 1 or abs(current_coord_H[1] - current_coord_T[1]) > 1:
                current_coord_T = copy(current_coord_H_prev)
            if current_coord_T not in coordinates:
                coordinates.append(current_coord_T)
    return len(coordinates)


def max1(val):
    return 1 if val == 2 else -1 if val == -2 else val


def move(pos1, pos2):
    vector = (0, 0)
    if abs(pos1[0] - pos2[0]) > 1:
        vector = (-1 if pos1[0] - pos2[0] < -1 else 1, max1(pos1[1] - pos2[1]))
    elif abs(pos1[1] - pos2[1]) > 1:
        vector = (max1(pos1[0] - pos2[0]), -1 if pos1[1] - pos2[1] < -1 else 1)
    if 0 not in vector:
        temp = [pos2[0]+vector[0], pos2[1]+vector[1]]
        pass
    return vector


def part2(inp):
    coordinates_9_visits = []
    current_coord_prevs = [[0, 0] for i in range(10)]
    current_coords = [[0, 0] for i in range(10)]
    for direction, number in inp:
        for _ in range(number):
            current_coord_prevs[0] = copy(current_coords[0])
            match direction:
                case "L":
                    current_coords[0][0] -= 1
                case "R":
                    current_coords[0][0] += 1
                case "U":
                    current_coords[0][1] += 1
                case "D":
                    current_coords[0][1] -= 1

            for num in range(1, len(current_coords)):
                current_coord_prevs[num] = copy(current_coords[num])
                vector = move(current_coords[num-1], current_coords[num])

                current_coords[num][0] += vector[0]
                current_coords[num][1] += vector[1]
            if current_coords[-1] not in coordinates_9_visits:
                coordinates_9_visits.append(copy(current_coords[-1]))
    return len(coordinates_9_visits)


print("Part 1: ", part1(parser()))
print("Part 2: ", part2(parser()))

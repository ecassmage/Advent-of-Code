def parser():
    output: list = []
    for line in open("input.txt"):
        line: list = line.strip().split(" ")
        if len(line) == 2:
            output.append([line[0], int(line[1])])
        else:
            output.append([line[0]])
    return output


def during_cycle_1():
    pass


def after_cycle_1(X, rule):
    if rule[0] == 'addx':
        return X + rule[1]
    return X


def part1(inp):
    cycle = 0
    summed = 0
    X = 1

    dictionary = {
        "noop": 1,
        "addx": 2
    }
    sprite = list(range(X - 1, X + 2))
    checkers = [20, 60, 100, 140, 180, 220]
    for rule in inp:
        timer = dictionary[rule[0]]
        ticker = 0
        while ticker < timer:
            ticker += 1
            cycle += 1
            if cycle in checkers:
                summed += (cycle * X)
        if rule[0] == 'addx':
            X += rule[1]
            pass

    return summed


def printo(inp):
    for line in inp:
        print(line)


def part2(inp):
    cycle = 0
    ptr = []
    output = []

    X = 1
    sprite = list(range(0, 3))
    dictionary = {
        "noop": 1,
        "addx": 2
    }

    # checkers = [20, 60, 100, 140, 180, 220]
    for rule in inp:
        timer = dictionary[rule[0]]
        ticker = 0
        while ticker < timer:

            if cycle % 40 == 0:
                ptr = []
                output.append(ptr)
                cycle = 0

            ptr.append("#" if cycle in sprite else ".")
            ticker += 1
            cycle += 1

        if rule[0] == 'addx':
            X += rule[1]
            sprite = list(range(X - 1, X + 2))

    return output


print("Part 1: ", part1(parser()))
print("Part 2: ", printo(part2(parser())))


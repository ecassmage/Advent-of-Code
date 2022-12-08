def parser():
    string = []

    with open("input.txt", 'r') as file:
        for line in file:
            line = line.strip()
            string.append([line[:int(len(line) / 2)], line[int(len(line) / 2):]])
            if len(line[:int(len(line) / 2)]) + len(line[int(len(line) / 2):]) != len(line):
                print(string[-1])
    return string


def part1():
    output = parser()
    summed = 0
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for grouping in output:
        comp_2 = list(grouping[1])
        both = []
        if len(grouping[0]) != len(grouping[1]):
            print(grouping)
        for char in grouping[0]:
            if char in comp_2:
                if char not in both:
                    both.append(char)
        summed += sum([string.index(char)+1 for char in both])
    return summed


def part2():
    parser()
    output = parser()
    summed = 0
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    groupings = []
    for num, grouping in enumerate(output):
        if num % 3 == 0:
            groupings.append([''.join(grouping)])
        else:
            groupings[-1].append(''.join(grouping))

    for group in groupings:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                summed += string.index(char)+1
                break

    return summed


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())

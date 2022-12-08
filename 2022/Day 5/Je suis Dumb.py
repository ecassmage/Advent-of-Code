def parser():
    state = 0
    boxes = []
    moves = []
    with open('input.txt') as file:
        for line in file:
            line = line[:-1] if line[-1] == '\n' else line
            if line == "":
                state += 1
                continue
            match state:
                case 0:
                    if '[' not in line:
                        continue
                    else:
                        for num, i in enumerate(range(1, len(line), 4)):
                            if len(boxes) == num:
                                boxes.append([])
                            if line[i] != ' ':
                                boxes[num].insert(0, str(line[i]))
                case 1:
                    string = line.split(' ')
                    moves.append([int(string[1]), int(string[3]), int(string[5])])
                    pass

    return boxes, moves


def move_boxes(boxes, number, row1, row2):
    stack = []
    for _ in range(number):
        stack.append(boxes[row1-1].pop())
    for char in reversed(stack):
        boxes[row2-1].append(char)


def part1(boxes, moves):
    for iterations, row1, row2 in moves:
        for _ in range(iterations):
            move_boxes(boxes, 1, row1, row2)
    for row in boxes:
        print(row)
    return ''.join([box[-1] for box in boxes])


def part2(boxes, moves):
    for iterations, row1, row2 in moves:
        move_boxes(boxes, iterations, row1, row2)

    return ''.join([box[-1] for box in boxes])


print("Part 1: ", part1(*parser()))
print("Part 2: ", part2(*parser()))

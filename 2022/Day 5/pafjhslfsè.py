def parser():
    state = 0
    boxes = []
    moves = []
    length = 0
    with open('input.txt') as file:
        for line in file:
            line = line[:-1] if line[-1] == '\n' else line
            if line == "":
                state += 1
                continue
            match state:
                case 0:
                    if '[' not in line:
                        a = (line.replace(' ', ''))
                        length = len(line.replace(' ', ''))
                        continue
                    else:
                        boxes.append([str(line[i]) for i in range(1, len(line), 4)])
                        pass
                case 1:
                    string = line.split(' ')
                    moves.append([int(string[1]), int(string[3]), int(string[5])])
                    pass

    return boxes, moves, length


def move_box_2000(boxes, row1, row2, length):
    row1_char = ''
    for row in boxes:
        if row[row1] != ' ':
            row1_char = row[row1]
            row[row1] = ' '
            break
    row_num = -1
    for row in boxes:
        if row[row2] != ' ':
            break
        row_num += 1
    if row_num == -1:
        boxes.insert(0, [' '] * length)
        row_num = 0
    boxes[row_num][row2] = row1_char
    pass


def move_box_2001(boxes, number_to_move, row1, row2, length):
    row1_char = []  # stack
    num_moved = 0
    for row in boxes:
        if row[row1] != ' ':
            row1_char.append(row[row1])
            row[row1] = ' '
            num_moved += 1
        if num_moved == number_to_move:
            break
    row_num = -1
    for row in boxes:
        if row[row2] != ' ':
            break
        row_num += 1
    if row_num - len(row1_char) < 0:
        for _ in range(abs(row_num - len(row1_char))):
            boxes.insert(0, [' '] * length)
            row_num += 1
    for num, char in enumerate(reversed(row1_char)):
        if boxes[row_num-num][row2] != ' ':
            pass
        boxes[row_num-num][row2] = char
        pass
    pass


def part1(boxes, moves, length):
    for iterations, row1, row2 in moves:
        for _ in range(iterations):
            move_box_2000(boxes, row1-1, row2-1, length)
            pass
        pass

    chars = [' '] * length

    for row in boxes:
        for num, col in enumerate(row):
            if chars[num] != ' ':
                continue
            elif col != ' ':
                chars[num] = col
    for row in boxes:
        print(row)
    return ''.join(chars)


def part2(boxes, moves, length):
    for iterations, row1, row2 in moves:
        move_box_2001(boxes, iterations, row1 - 1, row2 - 1, length)
        pass

    chars = [' '] * length

    for row in boxes:
        for num, col in enumerate(row):
            if chars[num] != ' ':
                continue
            elif col != ' ':
                chars[num] = col
    return ''.join(chars)


print("Part 1: ", part1(*parser()))
print("Part 2: ", part2(*parser()))


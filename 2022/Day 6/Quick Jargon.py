def parser():
    output = ''
    for line in open('input.txt'):
        output += line
    return output


def verify(stack):
    for num, char in enumerate(stack):
        if char in stack[num+1:]:
            return False
    return True


def part1(inp):
    stack = []
    for num, char in enumerate(inp):
        if len(stack) == 4:
            stack.pop(0)
        stack.append(char)
        if len(stack) == 4 and verify(stack):
            return num+1

    pass


def part2(inp):
    stack = []
    for num, char in enumerate(inp):
        if len(stack) == 14:
            stack.pop(0)
        stack.append(char)
        if len(stack) == 14 and verify(stack):
            return num + 1


print('Part 1: ', part1(parser()))
print('Part 2: ', part2(parser()))

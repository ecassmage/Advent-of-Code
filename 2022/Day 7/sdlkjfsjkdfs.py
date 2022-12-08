class Folder:
    def __init__(self, name, prev):
        self.name = name
        self.prev = prev
        self.contents = {}


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def parser():
    root = Folder("root", None)
    ptr = root
    for line in open('input.txt'):
        line = line.strip()
        if line[0] == '$':
            command_break = line.split(" ")
            match command_break[1]:
                case "cd":
                    match command_break[2]:
                        case "..":
                            ptr = ptr.prev
                            pass
                        case "/":
                            ptr = root
                            pass
                        case _:
                            ptr = ptr.contents[command_break[2]]
                            pass
                    pass
                case "ls":
                    pass
                case _:
                    pass
        else:
            line = line.split(" ")
            match line[0]:
                case "dir":
                    ptr.contents[line[1]] = Folder(line[1], ptr)
                case _:
                    ptr.contents[line[1]] = File(line[1], int(line[0]))
    return root


sizeMax = 100000


def part1(inp):
    total_that_fit = []
    contentSize = 0
    for item in inp.contents:
        if isinstance(inp.contents[item], Folder):
            total_that_fit_temp, contentSizeTemp = part1(inp.contents[item])
            total_that_fit = [*total_that_fit, *total_that_fit_temp]
            contentSize += contentSizeTemp
        else:
            contentSize += inp.contents[item].size
    if contentSize > sizeMax:
        return total_that_fit, contentSize
    return [*total_that_fit, contentSize], contentSize


def part2(inp):
    total_that_fit = []
    contentSize = 0
    for item in inp.contents:
        if isinstance(inp.contents[item], Folder):
            total_that_fit_temp, contentSizeTemp = part2(inp.contents[item])
            total_that_fit = [*total_that_fit, *total_that_fit_temp]
            contentSize += contentSizeTemp
        else:
            contentSize += inp.contents[item].size
    return [*total_that_fit, contentSize], contentSize


def part2_2(inp):
    output, out = part2(inp)
    output.sort()
    total_needed = out - 40000000
    for val in output:
        if val - total_needed >= 0:
            return val


print("Part 1: ", sum(part1(parser())[0]))
print("Part 2: ", part2_2(parser()))


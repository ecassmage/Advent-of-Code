def test() -> list:
    pass


def parser():
    arr: list = []
    arr = test()
    for line in open("input.txt"):
        arr.append([int(val) for val in list(line.strip())])
    return arr


def CheckDirections_p1(num1, num2, val, grid):
    for num in range(num1-1, -1, -1):
        if grid[num][num2] >= val:
            break
    else:
        return True

    for num in range(num1+1, len(grid)):
        if grid[num][num2] >= val:
            break
    else:
        return True

    for num in range(num2-1, -1, -1):
        if grid[num1][num] >= val:
            break
    else:
        return True

    for num in range(num2+1, len(grid[num1])):
        if grid[num1][num] >= val:
            break
    else:
        return True

    return False


def CheckDirections_p2(num1, num2, val, grid):
    def mult(arr):
        beau = 1
        for number in arr:
            beau *= number
        return beau

    beauty = []
    num_trees = 0
    for num in range(num1-1, -1, -1):
        num_trees += 1
        if grid[num][num2] >= val:
            break

    beauty.append(num_trees)
    num_trees = 0

    for num in range(num1+1, len(grid)):
        num_trees += 1
        if grid[num][num2] >= val:
            break

    beauty.append(num_trees)
    num_trees = 0

    for num in range(num2-1, -1, -1):
        num_trees += 1
        if grid[num1][num] >= val:
            break

    beauty.append(num_trees)
    num_trees = 0

    for num in range(num2+1, len(grid[num1])):
        num_trees += 1
        if grid[num1][num] >= val:
            break

    beauty.append(num_trees)

    return mult(beauty)

#
# def getValWrap(num1, num2, grid):
#     try:
#         if num1 < 0 or num2 < 0:
#             return None
#         return grid[num1][num2]
#     except IndexError:
#         return None
#
#
# def getSurroundings(num1, num2, grid):
#     vals = [getValWrap(num1-1, num2, grid), getValWrap(num1+1, num2, grid), getValWrap(num1, num2-1, grid), getValWrap(num1, num2+1, grid)]
#     return [getValWrap(num1-1, num2, grid), getValWrap(num1+1, num2, grid), getValWrap(num1, num2-1, grid), getValWrap(num1, num2+1, grid)]


def part1(inp):
    number = 0
    for num1, row in enumerate(inp):
        for num2, col in enumerate(row):
            if CheckDirections_p1(num1, num2, col, inp):
                number += 1
    return number


def part2(inp):
    number = 0
    for num1, row in enumerate(inp):
        for num2, col in enumerate(row):
            num = CheckDirections_p2(num1, num2, col, inp)
            if num > number:
                number = num
    return number


print("Part 1: ", part1(parser()))
print("Part 2: ", part2(parser()))

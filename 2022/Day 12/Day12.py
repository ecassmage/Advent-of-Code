from Mapo import Mapo


def S(heighto):
    S_class = None
    E_class = None
    for rowo in heighto:
        for mapo in rowo:
            if mapo.char == "S":
                S_class = mapo
            elif mapo.char == "E":
                E_class = mapo
    return S_class, E_class


def parser():
    height_map = []
    x = 0
    for line in open("input.txt"):
        height_map.append([Mapo(char, x, y) for y, char in enumerate(list(line.strip()))])
        x += 1

    for row_num, map_row in enumerate(height_map):
        for col_num, mapo in enumerate(map_row):
            mapo.setup(height_map, row_num, col_num)

    return height_map


def Trace(_S: Mapo, _E: Mapo) -> list:
    ptr = _E.prev
    array: list[Mapo] = []
    while ptr != _S:
        array.insert(0, ptr)
        ptr = ptr.prev
    return array


def AStar(_S, _E, height_map):
    opened = [_S]
    closed = []

    while len(opened) > 0:
        curr = opened[0]
        for mapo in opened:
            if mapo.f_cost() < curr.f_cost() or mapo.f_cost() == curr.f_cost() and mapo.h_cost < curr.h_cost:
                curr = mapo
        closed.append(opened.pop(opened.index(curr)))

        if curr == _E:
            return Trace(_S, _E)

        for neighbour in curr:
            if not neighbour.traversible(curr) or neighbour in closed:
                continue

            new_path = curr.g_cost + neighbour.distance(curr)
            if new_path < neighbour.g_cost or neighbour not in opened:
                neighbour.g_cost = new_path
                neighbour.h_cost = neighbour.distance(_E)
                neighbour.prev = curr

                if neighbour not in opened:
                    opened.append(neighbour)
    return []


def part1(inp):
    _S, _E = S(inp)
    a = AStar(_S, _E, inp)
    return len(a) + 1


def part2(inp):
    aaa = []
    _S, _E = S(inp)
    _S.char = 'a'
    for row in inp:
        for col in row:
            if col.char == 'a':
                aaa.append(col)
    shortest = -1
    print(len(aaa))
    for ele in aaa:
        ele.char = 'S'
        a = AStar(ele, _E, inp)
        if len(a) + 1 < shortest or shortest == -1:
            shortest = len(a) + 1

    return shortest


print("Print 1:", part1(parser()))
print("Print 2:", part2(parser()))

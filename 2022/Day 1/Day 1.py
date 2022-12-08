def part1():
    aro = []

    arr = []
    for num in open('input.txt'):
        num = num.strip()
        if num != '':
            arr.append(int(num))
        else:
            aro.append(sum(arr))
            arr = []
    aro.sort()
    return sum(aro[-3:])


if __name__ == '__main__':
    print("Part 1: " + str(part1()))

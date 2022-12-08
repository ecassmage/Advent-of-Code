def parser():
    return [line.strip().split(',') for line in open('input.txt')]


def part1():
    output = parser()
    num = 0
    for group in output:
        elf1 = group[0].split('-')
        elf1 = (int(elf1[0]), int(elf1[1]))
        elf2 = group[1].split('-')
        elf2 = (int(elf2[0]), int(elf2[1]))
        if (elf1[0] > elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] < elf2[0] and elf1[1] >= elf2[1]) or elf1[0] == elf2[0]:
            num += 1
    return num


def gen(nums1, nums2):
    for num in nums1:
        yield nums2[0], num, nums2[1]
    for num in nums2:
        yield nums1[0], num, nums1[1]


def part2():
    output = parser()
    num = 0
    for group in output:
        elf1 = group[0].split('-')
        elf1 = (int(elf1[0]), int(elf1[1]))
        elf2 = group[1].split('-')
        elf2 = (int(elf2[0]), int(elf2[1]))
        for n1, n2, n3 in gen(elf1, elf2):
            if n1 <= n2 <= n3:
                num += 1
                break
    return num


if __name__ == '__main__':
    print("Part 1: ", part1())
    print("Part 2: ", part2())
    pass


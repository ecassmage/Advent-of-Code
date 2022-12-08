def winner_winner_chicken_dinner(them, you):
    Lose = 0
    Draw = 3
    Win = 6
    match (them - you):
        case 0:
            return you + Draw
        case 1 | -2:
            return you + Lose
        case -1 | 2:
            return you + Win
    pass


def winner_winner_chicken_dinner_23(them, you):
    match you:
        case 1:
            a = winner_winner_chicken_dinner(them, them + 1 if them < 3 else 1)
            return winner_winner_chicken_dinner(them, them - 1 if them > 1 else 3)
        case 2:
            a = winner_winner_chicken_dinner(them, them)
            return winner_winner_chicken_dinner(them, them)
        case 3:
            a = winner_winner_chicken_dinner(them, them - 1 if them > 1 else 3)
            return winner_winner_chicken_dinner(them, them + 1 if them < 3 else 1)
    pass


def part1():
    dictionary = {
        'A': 1,  # R
        'B': 2,  # P
        'C': 3,  # S
        'X': 1,  # R
        'Y': 2,  # P
        'Z': 3,  # S
    }

    score = 0
    for line in open('input.txt'):
        them, you = line.strip().split(' ')
        score += winner_winner_chicken_dinner(dictionary[them], dictionary[you])
    return score


def part2():
    dictionary = {
        'A': 1,  # R
        'B': 2,  # P
        'C': 3,  # S
        'X': 1,  # R
        'Y': 2,  # P
        'Z': 3,  # S
    }

    score = 0
    for line in open('input.txt'):
        them, you = line.strip().split(' ')
        score += winner_winner_chicken_dinner_23(dictionary[them], dictionary[you])
    return score


if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())

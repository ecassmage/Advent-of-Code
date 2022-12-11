import re
import Monkey


def new_dict():
    return {
        "monkey_id": -1,
        "starting_items": [],
        "operation": '',
        "test": '',
        "true": '',
        "false": ''
    }


def parser():
    list_of_monkeys = []
    dictionary = None
    for line in open("input.txt"):
        line = line.strip()
        output = re.match("Monkey (?P<num>[0-9]+):", line)
        if output:
            if dictionary is not None:
                list_of_monkeys.append(Monkey.Monkey(**dictionary))
            dictionary = new_dict()
            dictionary['monkey_id'] = int(output.group('num'))
            continue
        output = line.split(":")
        match output[0].strip():
            case "Starting items":
                dictionary['starting_items'] = [int(ele) for ele in output[1].replace(" ", "").split(",")]
                pass
            case "Operation":
                dictionary['operation'] = output[1].strip()
                pass
            case "Test":
                dictionary['test'] = output[1].strip()

            case "If true":
                dictionary['true'] = output[1].strip()
                pass

            case "If false":
                dictionary['false'] = output[1].strip()
    list_of_monkeys.append(Monkey.Monkey(**dictionary))
    return list_of_monkeys


def Part1(monkies: list[Monkey.Monkey]):
    for i in range(20):
        for monkey in monkies:
            for item in monkey.items:
                worry_level: int = monkey.inspection(item)
                worry_level = int(worry_level / 3)
                pass_to = monkey.divisibility(worry_level)
                worry_level = worry_level % monkey.test[1]
                monkies[pass_to].items.append(worry_level)
            monkey.items = []
    inspections = []
    for monkey in monkies:
        inspections.append(monkey.inspections)
    inspections.sort()
    return inspections[-1] * inspections[-2]


def LCM(Monkies):
    lcm = 1
    for monkey in Monkies:
        lcm *= monkey.test[1]
    return lcm


def Part2(monkies):
    lcm = LCM(monkies)
    for i in range(10000):
        for monkey in monkies:
            for item in monkey.items:
                worry_level: int = monkey.inspection(item)
                # worry_level = int(worry_level / 3)
                pass_to = monkey.divisibility(worry_level)
                monkies[pass_to].items.append(worry_level)
            monkey.items = []
        print(f"Done {i}")
    inspections = []
    for monkey in monkies:
        inspections.append(monkey.inspections)
    inspections.sort()
    return inspections[-1] * inspections[-2]


print("Part 1:", Part1(parser()))
# print("Part 2:", Part2(parser()))

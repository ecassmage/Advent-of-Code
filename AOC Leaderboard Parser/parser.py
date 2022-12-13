import json
from Person import Person, LeaderBoard


def parser(path):
    file = json.load(open(path))
    new_dict: LeaderBoard = LeaderBoard()
    for data in dict(file['members']).values():
        new_dict.Add(Person(**data))

    new_dict.SortBy('local')
    pass


parser("1521876.json")
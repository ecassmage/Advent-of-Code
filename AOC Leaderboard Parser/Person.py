class Person:
    def __init__(self, local_score, global_score, completion_day_level, name, stars, last_star_ts, **kwargs):
        self.local_score = local_score
        self.global_score = global_score
        self.completion_day_level = completion_day_level
        self.name = name
        self.stars = stars
        self.last_star_ts = last_star_ts
        self.id = kwargs['id']

    def get_day(self, day: list[int], get_values: list[str] = None):
        if get_values is None: get_values = []
        data = {}
        if day == -1:
            pass
        else:
            pass
        pass

    @staticmethod
    def get_data_specified(dict_level, data_wanted):
        return {
            key: dict_level[key] for key in data_wanted
        }


class LeaderBoard:
    def __init__(self):
        self.manager: dict[str: Person] = { }

        self.total_days: int = 0

    def Add(self, person: Person):
        self.manager[person.name if person.name not in self.manager else person.id] = person

    def SortBy(self, code: str):
        match code.replace("_", '').replace(' ', '').lower():
            case "local":
                code = 'local_score'

            case 'global':
                code = 'global_score'

            case 'alphabetical':
                code = 'name'

            case _:
                pass
        for person in self.manager.values():
            person.get_day([1])
            pass



    def best_in_day(self, code: str, day: int):
        for person in self.manager.values():
            pass
        pass
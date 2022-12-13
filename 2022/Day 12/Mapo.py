class Mapo:
    def __init__(self, char, row, col):
        self.char = char
        self.North: Mapo = None
        self.East: Mapo = None
        self.South: Mapo = None
        self.West: Mapo = None

        self.g_cost = 0
        self.h_cost = 0
        self.prev: Mapo = None
        self.x = row
        self.y = col

    def setup(self, array, row, column):
        self.North = array[row - 1][column] if 0 <= row - 1 else None
        self.East = array[row][column + 1] if column + 1 < len(array[row]) else None
        self.South = array[row + 1][column] if row + 1 < len(array) else None
        self.West = array[row][column - 1] if 0 <= column - 1 else None

    def f_cost(self):
        self.f_costs = self.g_cost + self.h_cost
        return self.g_cost + self.h_cost

    def distance(self, val):
        return 10*(abs(self.x - val.x)) + 10*(abs(self.y - val.y))

    def __iter__(self):
        for mapo in [self.North, self.East, self.South, self.West]:
            if mapo is not None:
                yield mapo

    def traversible(self, other):
        if other.char == "S":
            return True
        if self.char == 'E' and other.char == 'z':
            return True
        return ord(self.char) - ord(other.char) < 2

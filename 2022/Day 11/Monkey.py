class Monkey:
    def __init__(self, monkey_id: int, starting_items: list, operation, test, true, false):
        self.id: int = monkey_id
        self.items: list[int] = starting_items
        self.operation: list[str, int] = self.parse_operation(operation)
        self.test = self.parse_test(test)
        self.true = self.parse_boolean(true)
        self.false = self.parse_boolean(false)

        self.inspections = 0
        pass

    @staticmethod
    def parse_operation(string: str) -> list[str, int]:
        out = string.split(" ")
        return [out[3], int(out[4]) if out[4] != 'old' else 'old']

    @staticmethod
    def parse_test(test: str):
        out = test.split(" ")
        return [out[0], int(out[2])]

    @staticmethod
    def parse_boolean(boolean):
        return int(boolean.split(" ")[-1])

    def inspection(self, worry) -> int:
        self.inspections += 1
        match self.operation[0]:
            case "+":
                return worry + (self.operation[1] if self.operation[1] != 'old' else worry)
            case "*":
                return worry * (self.operation[1] if self.operation[1] != 'old' else worry)
            case "-":
                return worry - (self.operation[1] if self.operation[1] != 'old' else worry)
            case "/":
                return int(worry / (self.operation[1] if self.operation[1] != 'old' else worry))

    def divisibility(self, worry):
        return self.true if worry % self.test[1] == 0 else self.false

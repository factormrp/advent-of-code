from models.source import Source
from typing import List, Tuple


class Monkey:
    def __init__(
        self,
        items: List[int],
        operation: str,
        throw_condition: int,
        target_true: int,
        target_false: int
    ) -> None:
        self.items = items
        self.operation = operation
        self.throw_condition = throw_condition
        self.target_true = target_true
        self.target_false = target_false
        self.inspect_count = 0


class Community:
    def __init__(
        self,
        members: List[Monkey],
        grt: int
    ) -> None:
        self.members = members
        self.grt = grt

    def get_most_active_monkeys(self) -> List[Monkey]:
        return sorted(
            self.members, key=lambda monkey: monkey.inspect_count, reverse=True
        )[:2]

    def run_monkey_business(self, worry: bool = False, rounds: int = 1) -> List[Monkey]:
        monkeys = self.members
        for _ in range(rounds):
            monkeys = self.update_items(worry)
        return monkeys

    def get_sum_monkey_business(self) -> int:
        first, second = self.get_most_active_monkeys()
        return first.inspect_count * second.inspect_count

    def update_items(self, worry: bool) -> List[Monkey]:
        monkeys = self.members
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                item = monkey.items.pop()

                # Inspect item
                val1, operand, val2 = monkey.operation.split()
                val1 = item if val1 == 'old' else int(val1)
                val2 = item if val2 == 'old' else int(val2)
                if operand == '+':
                    result_item = val1 + val2
                elif operand == '*':
                    result_item = val1 * val2
                elif operand == '-':
                    result_item = val1 - val2
                elif operand == '/':
                    result_item = val1 / val2
                if not worry:
                    result_item = result_item // 3
                else:
                    result_item = result_item % self.grt
                monkey.inspect_count += 1

                # Throw item
                if result_item % monkey.throw_condition == 0:
                    monkeys[monkey.target_true].items.append(result_item)
                else:
                    monkeys[monkey.target_false].items.append(result_item)

        return monkeys

# 2,713,310,158
# 2,645,397,782


def get_community(source: Source) -> Tuple[List[Monkey], int]:
    grt = 1
    # lines = source.lines
    lines = [
        "Monkey 0:",
        "Starting items: 79, 98",
        "Operation: new = old * 19",
        "Test: divisible by 23",
        "If true: throw to monkey 2",
        "If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "Starting items: 54, 65, 75, 74",
        "Operation: new = old + 6",
        "Test: divisible by 19",
        "If true: throw to monkey 2",
        "If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "Starting items: 79, 60, 97",
        "Operation: new = old * old",
        "Test: divisible by 13",
        "If true: throw to monkey 1",
        "If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "Starting items: 74",
        "Operation: new = old + 3",
        "Test: divisible by 17",
        "If true: throw to monkey 0",
        "If false: throw to monkey 1",
    ]
    monkeys = []

    while True:
        line = lines.pop(0)
        if line.startswith('Monkey'):
            items = [int(i) for i in lines.pop(0).split(': ')[1].split(',')]
            operation = lines.pop(0).split('= ')[1]
            throw_condition = int(lines.pop(0).split('by ')[1])
            grt *= throw_condition
            target_true = int(lines.pop(0).split('monkey ')[1])
            target_false = int(lines.pop(0).split('monkey ')[1])
            monkeys.append(
                Monkey(items, operation, throw_condition, target_true, target_false)
            )
        if not lines:
            break

    return monkeys, grt


def main1(source: Source) -> int:
    monkeys, grt = get_community(source)
    friends = Community(monkeys, grt)
    friends.run_monkey_business(worry=False, rounds=20)
    return friends.get_sum_monkey_business()


def main2(source: Source) -> int:
    monkeys, grt = get_community(source)
    friends = Community(monkeys, grt)
    friends.run_monkey_business(worry=True, rounds=10000)
    return friends.get_sum_monkey_business()

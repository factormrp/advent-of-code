from typing import List, Tuple
from models.source import Source

# Define global vars
CRATE_SIZE = 4


def _get_crates_from(line: str) -> List[str]:
    results = []
    for i in range(0, len(line)+1, CRATE_SIZE):
        sub_str = line[i:i+CRATE_SIZE]
        results.append(''.join([c for c in sub_str if c.isalpha()]))
    return results


def _get_move_from(line: str) -> Tuple[int, int, int]:
    nums = [int(s) for s in line.split(' ') if s.isdigit()]
    return nums[0], nums[1]-1, nums[2]-1


def _process_move_1(
    number: int, origin: int, destination: int, lists: List[List[str]]
) -> List[List[str]]:
    for i in range(number):
        lists[destination].append(lists[origin].pop())
    return lists


def _process_move_2(
    number: int, origin: int, destination: int, lists: List[List[str]]
) -> List[List[str]]:
    if number == 1:
        lists[destination].append(lists[origin].pop())
    else:
        tmp = []
        for i in range(number):
            tmp.append(lists[origin].pop())
        for i in range(len(tmp)):
            lists[destination].append(tmp.pop())
    return lists


def main1(source: Source) -> str:
    # Initialize stacks
    stacks = [[] for i in range((len(source.lines[0]) + 1) // CRATE_SIZE)]

    for line in source.lines:
        # Populate the stacks
        if '[' in line:
            for i, crate in enumerate(_get_crates_from(line)):
                if crate != '':
                    stacks[i].insert(0, crate)
        # Skip
        elif line.replace(' ', '').isdigit() or line.replace(' ', '') == '':
            continue
        # Process moves
        else:
            num, start, end = _get_move_from(line)
            stacks = _process_move_1(num, start, end, stacks)

    # Aggregate result
    return ''.join([stack[-1] for stack in stacks])


def main2(source: Source) -> str:
    # Initialize stacks
    stacks = [[] for i in range((len(source.lines[0]) + 1) // CRATE_SIZE)]

    for line in source.lines:
        # Populate the stacks
        if '[' in line:
            for i, crate in enumerate(_get_crates_from(line)):
                if crate != '':
                    stacks[i].insert(0, crate)
        # Skip
        elif line.replace(' ', '').isdigit() or line.replace(' ', '') == '':
            continue
        # Process moves
        else:
            num, start, end = _get_move_from(line)
            stacks = _process_move_2(num, start, end, stacks)

    # Aggregate result
    return ''.join([stack[-1] for stack in stacks])

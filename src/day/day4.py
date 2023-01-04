from util.source import Source
from typing import List


def _get_pairs(line: str) -> List[int]:
    return [int(i) for i in line.split('-')]


def _is_fully_overlapping_pair(first: List[int], second: List[int]) -> bool:
    if (second[1] >= first[0] >= second[0] and first[1] <= second[1]) or (
        first[1] >= second[0] >= first[0] and second[1] <= first[1]
    ):
        return True
    return False


def _is_overlapping_pair(first: List[int], second: List[int]) -> bool:
    # import pdb
    # pdb.set_trace()
    if first[0] <= second[1] and first[1] >= second[0]:
        return True
    return False


def main1(source: Source) -> int:
    total = 0
    for line in source.lines:
        elf1, elf2 = line.split(',')
        elf1_list = _get_pairs(elf1)
        elf2_list = _get_pairs(elf2)
        if _is_fully_overlapping_pair(elf1_list, elf2_list):
            total += 1
    return total


def main2(source: Source) -> int:
    total = 0
    for line in source.lines:
        elf1, elf2 = line.split(',')
        elf1_list = _get_pairs(elf1)
        elf2_list = _get_pairs(elf2)
        if _is_overlapping_pair(elf1_list, elf2_list):
            total += 1
    return total

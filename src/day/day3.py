from util.source import Source
from typing import List
import itertools as it

HOW_MANY = 2


def _split_line_into(line: str, how_many: int) -> List[set]:
    results = []
    length = len(line)//how_many
    for i in range(how_many):
        results.append(set(it.islice(line, length*i, length*(i+1))))
    return results


def _get_intersection_of(iterable: List[set]) -> str:
    """Gets the intersection of all iterables"""
    first = iterable[0]
    inter = first.intersection(*iterable[1:])
    return inter.pop()


def _find_shared_item(bucket: List[str]) -> str:
    """
    Finds the item that is present in all strings

    Gets splits and finds their intersection
    """
    if len(bucket) == 1:
        splits = _split_line_into(bucket[0], HOW_MANY)
    else:
        splits = [set(line) for line in bucket]
    return _get_intersection_of(splits)


def _get_item_priority(item: str) -> int:
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        return 0


def main1(source: Source) -> int:
    total = 0
    for line in source.lines:
        item = _find_shared_item([line])
        total += _get_item_priority(item)
    return total


def main2(source: Source) -> int:
    # import pdb
    # pdb.set_trace()

    priorities, items = [], []
    bucket = []
    for i, line in enumerate(source.lines, 1):
        if i % 3 == 0:
            bucket.append(line)
            item = _find_shared_item(bucket)
            items.append(item)
            priorities.append(_get_item_priority(item))
            bucket = []
        else:
            bucket.append(line)
    return sum(priorities)

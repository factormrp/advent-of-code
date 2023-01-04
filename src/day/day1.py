from util.source import Source
from typing import List, Union


def _aggregate_data(data: Union[List[str], List[int]]) -> List[int]:
    counts = [0]
    for num in data:
        if num not in ["", " "]:
            counts[-1] += int(num)
        else:
            counts.append(0)
    return counts


def _get_top_n_from_data(
    data: List[int],
    n: int = 1
) -> List[int]:
    results = []
    tmp = data.copy()
    for i in range(n):
        m = max(tmp)
        tmp.pop(tmp.index(m))
        results.append(m)
    return results


def _get_sum_of_top_n(lines: List[str], n: int) -> int:
    # Pull data from today and aggregate sums
    agg = _aggregate_data(lines)

    # Select top n from aggregated data and report
    top = _get_top_n_from_data(agg, n)
    return sum(top)


def main1(source: Source) -> int:
    return _get_sum_of_top_n(source.lines, 1)


def main2(source: Source):
    return _get_sum_of_top_n(source.lines, 3)

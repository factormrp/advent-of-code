from typing import List, Union
from util.source import Source
import datetime as dt


def aggregate_data(data: Union[List[str], List[int]]) -> List[int]:
    counts = [0]
    for num in data:
        if num not in ["", " "]:
            counts[-1] += int(num)
        else:
            counts.append(0)
    return counts


def get_top_n_from_data(
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


def main():
    # Define today
    today = dt.datetime(2022, 12, 1)

    # Pull data from today and aggregate sums
    source = Source(today)
    split = source.lines
    agg = aggregate_data(split)

    # Select top n from aggregated data and report
    n = 3
    top = get_top_n_from_data(agg, n)
    print(f"The top {n} Calorie holders have {aggregate_data(top)}")


if __name__ == "__main__":
    main()

from typing import List, Union
from util.source import Source
import datetime as dt

from util.source import Source
from typing import List
import datetime as dt
import argparse
import sys


def parse_args(arguments: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("question", choices=["1", "2"])
    return parser.parse_args(arguments)


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

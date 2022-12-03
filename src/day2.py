from util.source import Source
from typing import List
import datetime as dt
import argparse
import sys


def parse_args(arguments: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("question", choices=["1", "2"])
    return parser.parse_args(arguments)


def get_shape(strategy: str) -> str:
    shapes = {
        "A": "rock",
        "X": "rock",
        "B": "paper",
        "Y": "paper",
        "C": "scissors",
        "Z": "scissors"
    }
    return shapes[strategy.upper()]


def get_corresponding_shape(shape: str, predetermined: str) -> str:
    if predetermined.upper() == "Y":
        return shape

    outcomes = {
        "X": {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        },
        "Z": {
            "scissors": "rock",
            "rock": "paper",
            "paper": "scissors"
        }
    }
    return outcomes[predetermined.upper()][shape]


def calc_winner(shape_one: str, shape_two: str) -> int:
    """Determine winner by comparing the shapes used"""
    if shape_one == shape_two:
        return 3
    win_a = (shape_two == "scissors" and shape_one == "paper")
    win_b = (shape_two == "paper" and shape_one == "rock")
    win_c = (shape_two == "rock" and shape_one == "scissors")
    if win_a or win_b or win_c:
        return 6
    return 0


def calc_winner_from_outcome(predetermined: str) -> int:
    if predetermined.upper() == "X":
        return 0
    elif predetermined.upper() == "Y":
        return 3
    return 6


def _calc_shape_score(shape: str) -> int:
    if shape == "rock":
        return 1
    if shape == "paper":
        return 2
    return 3


def calc_score(strategy_one: str, strategy_two: str) -> int:
    # Get corresponding shapes
    shape_one = get_shape(strategy_one)
    shape_two = get_shape(strategy_two)
    # Determine winner
    return _calc_shape_score(shape_two) + calc_winner(shape_one, shape_two)


def calc_score_with_predetermined(strategy_one: str, outcome: str) -> int:
    # Get corresponding shapes
    shape_one = get_shape(strategy_one)
    shape_two = get_corresponding_shape(shape_one, outcome)
    # Determine winner
    return _calc_shape_score(shape_two) + calc_winner_from_outcome(outcome)


def main1(input_data: List[str]) -> int:
    """Logic to answer Question #1"""
    # Initialize count of my score
    running_total = 0

    # Process each line
    for line in input_data:
        p1 = line.split(" ")[0]
        p2 = line.split(" ")[1]
        score = calc_score(p1, p2)
        running_total += score

    return running_total


def main2(input_data: List[str]) -> int:
    """Logic to answer Question #2"""
    # Initialize count of my score
    running_total = 0

    # Process each line
    for line in input_data:
        p1 = line.split(" ")[0]
        result = line.split(" ")[1]
        score = calc_score_with_predetermined(p1, result)
        running_total += score

    return running_total


if __name__ == "__main__":
    # Get passed arguments
    args = parse_args(sys.argv[1:])

    # Fetch data
    today = dt.datetime(2022, 12, 2)
    source = Source(today)
    lines = source.lines

    if args.question == "1":
        total = main1(lines)
    else:
        total = main2(lines)

    # Report results
    print(f"Final score for me is: {total}")

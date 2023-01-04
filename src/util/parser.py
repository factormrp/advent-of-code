from typing import List
import argparse


def parse_args(arguments: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("question", type=str, choices=["1", "2"])
    parser.add_argument("-M", "--manual", type=str, action='store')
    return parser.parse_args(arguments)

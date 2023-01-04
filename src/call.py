from util.parser import parse_args
from util.source import Source
from typing import Callable
import importlib as imp
import datetime as dt
import logging as log
import pdb
import sys
import os

# Define today
today = dt.datetime.today()

# Configure logger
logger = log.getLogger(__name__)
logger.setLevel(log.DEBUG)
fh = log.FileHandler(os.path.join('..', 'logs', f'day{today.day}.log'))
fh.setLevel(log.DEBUG)
ch = log.StreamHandler()
ch.setLevel(log.ERROR)
formatter = log.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


def get_mod(tip: int) -> Callable[[Source], int]:
    """Dynamically import main implementation"""
    frmt = today.day
    try:
        module = imp.import_module(f"day.day{frmt}")
        mod: Callable[[Source], int] = getattr(module, f"main{tip}")
    except (ImportError, AttributeError):
        raise ValueError(f"Unknown format {frmt!r}") from None
    return mod


if __name__ == "__main__":
    logger.info("=== Advent of Code ===")
    try:
        logger.info("Parse commandline arguments...")
        args = parse_args(sys.argv[1:])

        if args.manual:
            today = dt.datetime.fromisoformat(args.manual)

        logger.info("Pull data from today and get lines...")
        source = Source(today)

        logger.info(f"Call implementation {args.question}...")
        main = get_mod(args.question)
        result = main(source)

        print(f"Result: {result}")

    except ValueError:
        logger.info("Something went wrong?")

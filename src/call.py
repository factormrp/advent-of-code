import datetime as dt
import importlib as imp
import logging as log
from models.source import Source
import os
import sys
from typing import Callable
from util.parser import parse_args

# Parse commandline arguments
args = parse_args(sys.argv[1:])

# Define today
if args.manual:
    today = dt.datetime.fromisoformat(args.manual)
else:
    today = dt.datetime.today()


# Configure logger
logger = log.getLogger(__name__)
logger.setLevel(log.DEBUG)
fh = log.FileHandler(
    os.path.join(os.path.dirname(__file__), '..', 'logs', f'day{today.day}.log')
)
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
    except (ImportError, AttributeError) as e:
        logger.error(f'Raw error: {e}')
        raise ValueError(f"Unknown format {frmt!r}") from None
    return mod


if __name__ == '__main__':
    logger.info('=== Advent of Code ===')
    try:
        logger.info(f'Pull data from {today} and get lines...')
        source = Source(today)

        logger.info(f'Call implementation {args.question}...')
        main = get_mod(args.question)
        result = main(source)

        print(f'Result: {result}')

    except ValueError as e:
        logger.error('Something went wrong?')
        logger.error(e)
    except EnvironmentError as e:
        logger.error('Something went wrong?')
        logger.error(e)

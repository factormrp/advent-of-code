from util.source import Source

WINDOW_SIZE = 4
MESSAGE_LENGTH = 14


def _find_start_of_message(line: str, seek: int) -> int:
    for i in range(len(line)):
        if len(set(line[i:i+seek])) == seek:
            return i + seek
    return -1


def main1(source: Source) -> int:
    return _find_start_of_message(source.data, WINDOW_SIZE)


def main2(source: Source) -> int:
    return _find_start_of_message(source.data, MESSAGE_LENGTH)

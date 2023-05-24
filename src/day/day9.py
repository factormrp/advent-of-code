from models.source import Source


def move_head(head_pos: tuple, direction: str, distance: int) -> tuple:
    if direction == 'U':
        return head_pos[0], head_pos[1] + distance
    elif direction == 'R':
        return head_pos[0] + distance, head_pos[1]
    elif direction == 'D':
        return head_pos[0], head_pos[1] - distance
    elif direction == 'L':
        return head_pos[0] - distance, head_pos[1]


def is_adjacent(head_pos: tuple, tail_pos: tuple) -> bool:
    if abs(head_pos[0] - tail_pos[0]) <= 1 and abs(head_pos[1] - tail_pos[1]) <= 1:
        return True
    return False


def move_tail(head_pos: tuple, tail_pos: tuple) -> tuple:
    diff_x = head_pos[0] - tail_pos[0]
    diff_y = head_pos[1] - tail_pos[1]
    if diff_x > 0:
        new_x = tail_pos[0] + 1
    elif diff_x < 0:
        new_x = tail_pos[0] - 1
    elif diff_x == 0:
        new_x = tail_pos[0]
    if diff_y > 0:
        new_y = tail_pos[1] + 1
    elif diff_y < 0:
        new_y = tail_pos[1] - 1
    elif diff_y == 0:
        new_y = tail_pos[1]
    return new_x, new_y


def update_tail(head_pos: tuple, tail_pos: tuple) -> tuple:
    if not is_adjacent(head_pos, tail_pos):
        return move_tail(head_pos, tail_pos)
    return tail_pos


def main1(source: Source) -> int:
    seen = set()
    head_pos = (0, 0)
    tail_pos = (0, 0)

    for line in source.lines:
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            head_pos = move_head(head_pos, direction, 1)
            tail_pos = update_tail(head_pos, tail_pos)
            seen.add(tail_pos)

    return len(seen)


def main2(source: Source) -> int:
    seen = set()
    head_pos = (0, 0)
    one_pos = (0, 0)
    two_pos = (0, 0)
    three_pos = (0, 0)
    four_pos = (0, 0)
    five_pos = (0, 0)
    six_pos = (0, 0)
    seven_pos = (0, 0)
    eight_pos = (0, 0)
    tail_pos = (0, 0)

    for line in source.lines:
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            head_pos = move_head(head_pos, direction, 1)
            one_pos = update_tail(head_pos, one_pos)
            two_pos = update_tail(one_pos, two_pos)
            three_pos = update_tail(two_pos, three_pos)
            four_pos = update_tail(three_pos, four_pos)
            five_pos = update_tail(four_pos, five_pos)
            six_pos = update_tail(five_pos, six_pos)
            seven_pos = update_tail(six_pos, seven_pos)
            eight_pos = update_tail(seven_pos, eight_pos)
            tail_pos = update_tail(eight_pos, tail_pos)
            seen.add(tail_pos)

    return len(seen)

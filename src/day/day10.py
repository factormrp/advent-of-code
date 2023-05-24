from typing import List, Tuple
from models.source import Source

# Define global vars
CYCLES_OF_INTEREST = [20, 60, 100, 140, 180, 220]


def update_signal_strength(strength: int, cycle: int, register: int) -> int:
    if cycle in CYCLES_OF_INTEREST:
        # print(f'Cycle {cycle}: Register = {register}')
        strength += register * cycle
    return strength


def update_register(queue: List[int], register: int) -> Tuple[List[int], int]:
    val = queue.pop()
    register += val
    # print(f'Cycle {cycle}: Adding Value {val} such that Register = {register}')
    return queue, register


def process_command(queue: List[int], lines: List[str]) -> List[int]:
    line = lines.pop(0)
    if line != 'noop':
        _, val = line.split()
        queue.append(int(val))
    return queue


def main1(source: Source) -> int:

    # Define local vars
    add_queue = []
    cycle = 1
    lines = source.lines
    register = 1
    signal_strength = 0

    while True:
        # Check if we are at a cycle of interest
        signal_strength = update_signal_strength(signal_strength, cycle, register)

        # If last command was add, add to register
        if add_queue:
            add_queue, register = update_register(add_queue, register)

        # Otherwise, get next command
        elif lines:
            add_queue = process_command(add_queue, lines)

        # Update cycle clock
        cycle += 1

        # Check if we are done
        if cycle > 220:
            break

    return signal_strength


def update_grid(grid: List[List[str]], cycle: int, register: int) -> List[List[str]]:
    pixel = (cycle-1) % 40
    grid_level = (cycle-1) // 40
    # print(
    #     f'Cycle: {cycle},\tPixel: {pixel},\tRegister: {register},\tLevel: {grid_level}'
    # )
    if abs(pixel - register) <= 1:
        grid[grid_level].append('#')
    else:
        grid[grid_level].append('.')
    return grid


def main2(source: Source) -> int:

    # Define local vars
    add_queue = []
    cycle = 1
    grid: List[List[str]] = [[],[],[],[],[],[]]
    lines = source.lines
    register = 1

    while True:
        # Check if pixel should be drawn
        grid = update_grid(grid, cycle, register)

        # If last command was add, add to register
        if add_queue:
            add_queue, register = update_register(add_queue, register)

        # Otherwise, get next command
        elif lines:
            add_queue = process_command(add_queue, lines)

        # Update cycle clock
        cycle += 1

        # Check if we are done
        if cycle > 240:
            break

    for row in grid:
        print(''.join(row))
    return 0


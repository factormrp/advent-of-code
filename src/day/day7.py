# System imports
from typing import List
import os
# Custom imports
from util.source import Source

# Define global variables
filesys = {}
dirs = {'/'}
SP_D = 70000000
SP_NEED = 30000000


def _modify_cwd(current: str, target: str) -> str:
    if target == '/':
        return target
    elif target == '..':
        return os.path.split(current)[0]
    else:
        return os.path.join(current, target)


def _set_absolutes(file_list: List[str], directory: str) -> None:
    for file in file_list:
        meta, name = file.split(' ')
        if meta.isnumeric():
            filesys[os.path.join(directory, name)] = int(meta)
        else:
            dirs.add(os.path.join(directory, name))


def _handle_cmd(line: str, current_dir: str) -> str:
    if line[:2] == 'cd':
        target_dir = line[2:].replace('\n', '').strip()
        current_dir = _modify_cwd(current_dir, target_dir)

    if line[:2] == 'ls':
        files_w_meta = [i.strip() for i in line[3:].split('\n') if i != '']
        _set_absolutes(files_w_meta, current_dir)

    return current_dir


def _calc_size(directory: str) -> int:
    total_size = 0
    for file, size in filesys.items():
        if os.path.split(file)[0][:len(directory)] == directory:
            total_size += size
    return total_size


def _calc_size_of_dirs_of_interest() -> int:
    total_size = 0
    for dir in dirs:
        size = _calc_size(dir)
        if size <= 100000:
            total_size += size
    return total_size


def _calc_size_of_dir_to_delete() -> int:
    dir_sizes = [
        _calc_size(d) for d in dirs
        if _calc_size(d) >= SP_NEED - (SP_D - _calc_size('/'))
    ]
    return min(dir_sizes)


def main1(source: Source) -> int:
    cwd = '/'
    cmd_lines = [i.strip() for i in source.data().split('$') if i != '']
    for line in cmd_lines:
        cwd = _handle_cmd(line, cwd)

    return _calc_size_of_dirs_of_interest()


def main2(source: Source) -> int:
    cwd = '/'
    cmd_lines = [i.strip() for i in source.data().split('$') if i != '']
    for line in cmd_lines:
        cwd = _handle_cmd(line, cwd)

    return _calc_size_of_dir_to_delete()


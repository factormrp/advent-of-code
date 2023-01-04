# System imports
from typing import Set, List
import os
# Custom imports
from util.source import Source

final_line = '-1 inf'
filesys = {}
dirs = {'/'}


def _modify_cwd(current: str, target: str) -> str:
    if target == '/':  # AHHHHHH
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
        files_as_absolutes = _set_absolutes(files_w_meta, current_dir)

    return current_dir

def _calc_size(directory: str) -> int:
    total_size = 0
    for file, size in filesys.items():
        if os.path.split(file)[0] == directory:
            total_size += size
    return total_size


def _calc_size_of_dirs_of_interest() -> int:
    total_size = 0
    for dir in dirs:
        size = _calc_size(dir)
        if size < 100000:
            total_size += size
    return total_size


def main1(source: Source) -> int:
    try:
        cwd = '/'
        cmd_lines = [i.strip() for i in source.data.split('$') if i != '']
        #cmd_lines = [
        #    'ls\n205200 hnbqlmmg\n80316 lmw.zmd\ndir mwj\n122312 tsrwvqbg.tzh',
        #    'cd mwj',
        #    'ls\n99000 test.txt'
        #]
        for line in cmd_lines:
            cwd = _handle_cmd(line, cwd)

        return _calc_size_of_dirs_of_interest()
    except Exception as e:
        raise(e)

def main2(source: Source) -> int:
    pass

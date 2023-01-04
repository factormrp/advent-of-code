# System imports
from typing import List
import pdb
import os
# Custom imports
from util.source import Source

# Define global variables
filesys = {}
dirs = {'/'}


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
        if directory in os.path.split(file)[0]:
            total_size += size
    return total_size


def _calc_size_of_dirs_of_interest() -> int:
    total_size = 0
    for dir in dirs:
        size = _calc_size(dir)
        if size <= 100000:
            total_size += size
    return total_size


def main1(source: Source) -> int:
    cwd = '/'
    cmd_lines = [i.strip() for i in source.data.split('$') if i != '']
    #cmd_lines = ['cd /', 'ls\ndir a', 'cd a', 'ls\ndir a\n2 a.txt', 'cd a', 'ls\n99999 a.txt']
    #cmd_lines = ['cd /', 'ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d', 'cd a', 'ls\ndir e\n29116 f\n2557 g\n62596 h.lst', 'cd e', 'ls\n584 i', 'cd ..', 'cd ..', 'cd d', 'ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k']
    for line in cmd_lines:
        cwd = _handle_cmd(line, cwd)

    return _calc_size_of_dirs_of_interest()

def main2(source: Source) -> int:
    pass

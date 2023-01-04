from typing import List, Dict, Tuple, Union
from util.source import Source
import pdb


class Folder:
    def __init__(
        self,
        parent,
        children: List,
        directory_name: str
    ) -> None:
        self.parent = parent
        self.children = children
        self.absolute_name = f'{parent.absolute_name}/{directory_name}' \
            if parent is not None else directory_name
        self.relative_name = directory_name

    def add_child(self, child) -> None:
        self.children.append(child)

    def get_child(self, name):
        for child in [c for c in self.children if type(c)==self.__class__]:
            if child.relative_name == name:
                return child
        return None

    def __eq__(self, other) -> bool:
        try:
            return True if self.relative_name == other.relative_name else False
        except AttributeError:
            return True if self.relative_name == other else False

    def __repr__(self) -> str:
        return self.relative_name


def _handle_cd(arguments: str) -> str:
    return arguments.replace('\n', '').strip()


def _handle_ls(
    arguments: str, filesystem: Dict, current_dir: str
) -> Tuple[Dict, str]:
    pass


def _handle_cmd(
    line: str, filesystem: Folder, current_dir: str
) -> Tuple[Folder, str]:
    # DEBUG
    pdb.set_trace()
    if line[:2] == 'cd':
        target_dir = _handle_cd(line[2:])
        if target_dir == '/':  # AHHHHHH
            current_dir = target_dir
        elif target_dir == '..':
            filesystem = filesystem.parent
            current_dir = filesystem.relative_name
        elif target_dir not in filesystem.children:
            filesystem.add_child(Folder(filesystem, [], target_dir))
            filesystem = filesystem.children
        current_dir = target_dir

    if line[:2] == 'ls':
        files_found = [i.strip() for i in line[3:].split('\n') if i != '']
    return filesystem, current_dir


def main1(source: Source) -> int:
    cwd = '/'
    filesys = Folder(None, [], cwd)
    # lines = [i.strip() for i in source.data.split('$') if i != '']
    lines = ['ls\n205200 hnbqlmmg\n80316 lmw.zmd\ndir mwj\n122312 tsrwvqbg.tzh']
    for line in lines:
        filesys, cwd = _handle_cmd(line, filesys, cwd)
    return 1


def main2(source: Source) -> int:
    pass

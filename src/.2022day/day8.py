from models.source import Source


def _get_grids(source: Source) -> tuple[list[list[int]], list[list[int]]]:
    r_grid: list = []
    c_grid: list = []
    tmp: list = []

    for c in source.data(clean=False):
        if c == '\n':
            r_grid.append(tmp)
            if len(c_grid) != len(tmp):
                c_grid = [[t] for t in tmp]
            else:
                for i, t_c in enumerate(tmp):
                    c_grid[i].append(int(t_c))
            tmp = []
        elif c not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            raise ValueError(f'Parser improperly configured: Error char: {c}')
        else:
            tmp.append(int(c))
    return r_grid, c_grid


def get_neighbors(
    row_grid: list[list[int]],
    col_grid: list[list[int]],
    row_pos: int,
    col_pos: int,
) -> tuple[tuple, tuple]:
    # Identify the cardinal neighbor lists
    tmp_row_left = row_grid[row_pos][:col_pos]
    tmp_row_right = row_grid[row_pos][col_pos+1:]
    tmp_col_left = col_grid[col_pos][:row_pos]
    tmp_col_right = col_grid[col_pos][row_pos+1:]

    # Assign values normally, unless there are no cardinal neighbors
    row_neighbors = (
        tmp_row_left if tmp_row_left else [-1],
        tmp_row_right if tmp_row_right else [-1]
    )
    col_neighbors = (
        tmp_col_left if tmp_col_left else [-1],
        tmp_col_right if tmp_col_right else [-1]
    )
    return row_neighbors, col_neighbors


def is_visible(
    tree_height: int,
    hzntl_neighbors: tuple[list[int], list[int]],
    vert_neighbors: tuple[list[int], list[int]]
) -> bool:
    try:
        if (
            tree_height > max(hzntl_neighbors[0])     # west
            or tree_height > max(hzntl_neighbors[1])  # east
            or tree_height > max(vert_neighbors[0])   # north
            or tree_height > max(vert_neighbors[1])   # south
        ):
            return True
        return False
    except ValueError:
        raise ValueError(f'Improper neighbor assignment')


def _calc_scenic_score(height: int, direction: list[int]) -> int:
    tmp = direction.copy()
    score = 0
    while tmp:
        elem = tmp.pop()
        if elem == -1:
            return 0
        elif elem < height:
            score += 1
        else:
            score += 1
            break
    return score


def get_scenic_score(
    tree_height: int,
    hzntl_neighbors: tuple[list[int], list[int]],
    vert_neighbors: tuple[list[int], list[int]]
) -> int:
    west, east = hzntl_neighbors[0], hzntl_neighbors[1][::-1]
    north, south = vert_neighbors[0], vert_neighbors[1][::-1]
    west_score = _calc_scenic_score(tree_height, west)
    east_score = _calc_scenic_score(tree_height, east)
    north_score = _calc_scenic_score(tree_height, north)
    south_score = _calc_scenic_score(tree_height, south)
    return west_score * east_score * north_score * south_score


def main1(source: Source) -> int:
    rows, cols = _get_grids(source)
    trees_per_row = len(rows[0])
    visible_trees = 0
    for i in range(trees_per_row * trees_per_row):
        j = i // trees_per_row  # row position
        k = i % trees_per_row   # column position
        current_tree_height = rows[j][k]

        # Identify cardinal neighbors
        north_south, west_east = get_neighbors(rows, cols, j, k)

        if is_visible(current_tree_height, west_east, north_south):
            visible_trees += 1

    return visible_trees


def main2(source: Source) -> int:
    rows, cols = _get_grids(source)
    trees_per_row = len(rows[0])
    max_scenic_score = 0

    for i in range(trees_per_row * trees_per_row):
        j = i // trees_per_row  # row position
        k = i % trees_per_row  # column position
        current_tree_height = rows[j][k]

        # Identify cardinal neighbors
        north_south, west_east = get_neighbors(rows, cols, j, k)
        score = get_scenic_score(current_tree_height, west_east, north_south)
        if score > max_scenic_score:
            max_scenic_score = score

    return max_scenic_score

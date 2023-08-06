import pprint
from typing import Callable, Any, Tuple, List, Dict
import numpy as np

state_mapper = {
        0: [],
        1: [(2, 3)],
        2: [(1, 2)],
        3: [(1, 3)],
        4: [(0, 1)],
        5: [(0, 3), (1, 2)],
        6: [(0, 2)],
        7: [(0, 3)],
        8: [(0, 3)],
        9: [(0, 2)],
        10: [(0, 1), (2, 3)],
        11: [(0, 1)],
        12: [(1, 3)],
        13: [(1, 2)],
        14: [(2, 3)],
        15: [],
    }


def qualify_corners(corners: Tuple[Any, ...], qualifier: Callable[[Any], bool]) -> Tuple[bool, ...]:
    if len(corners) > 4:
        corners = corners[:4]

    return tuple(map(qualifier, corners))

def lines_state_from_qualified_corners(a, b, c, d):
    # return 1*a + 2*b +4*c+8*d
    calc_state = 8 * a + 4 * b + 2 * c + 1 * d
    return line_state_switch(calc_state)

def line_state_switch(state):
    return state_mapper.get(state, [])

def square_midpoints(x, y, w, h):
    tm = (x + w/2, y)
    rm = (x + w, y + h / 2)
    bm = (x + w/2, y + h)
    lm = (x, y + h / 2)

    return (tm, rm, bm, lm)

def line_state_of_corners(corner_vals, qualifier):
    qualified_corners = qualify_corners(corners=corner_vals, qualifier=qualifier)
    line_state = lines_state_from_qualified_corners(*qualified_corners)
    return line_state

def marching_squares(value_array: np.ndarray,
                     qualifier: Callable[[Any], bool]) -> Dict[Tuple[int, int],
                                                               List[Tuple[int, int]]]:
    r, c = value_array.shape

    ret = {}
    for ii in range(r-1):
        for jj in range(c-1):
            ret[ii, jj] = line_state_of_corners((value_array[ii, jj],
                                                 value_array[ii][jj + 1],
                                                 value_array[ii + 1][jj+1],
                                                 value_array[ii + 1][jj]),
                                                qualifier
                                                )
    return ret

def line_definitions_in_square(x, y, w, h, qualifier, corner_vals):
    line_state = line_state_of_corners(corner_vals, qualifier)
    descriptors = line_definition_on_square_from_line_state(x, y, w, h, line_state)
    return descriptors

def line_definition_on_square_from_line_state(x, y, w, h, lines):
    midpoints = square_midpoints(x, y, w, h)

    descriptors = []
    for line in lines:
        descriptors.append((midpoints[line[0]], midpoints[line[1]]))
    return descriptors

def line_definitions(x, y, w, h,
                     marching_squares: Dict[Tuple[int, int], List[Tuple[int, int]]]) -> Dict[Tuple[int, int],
                                                                                             List[Tuple[Tuple[float, float], Tuple[float, float]]]]:
    ret = {}

    for ind, lines in marching_squares.items():
        ret[ind] = line_definition_on_square_from_line_state(x, y, w, h, lines)

    return ret

def line_definitions_for_array(arr, x, y, w, h, qualifier) -> Dict[Tuple[int, int],
                                                             List[Tuple[Tuple[float, float], Tuple[float, float]]]]:
    msqrs = marching_squares(arr, qualifier)
    line_defs = line_definitions(x, y, w, h, msqrs)

    return line_defs


if __name__ == "__main__":
    import pprint
    import time

    x, y, w, h = 10, 20, 10, 10
    qualifier = lambda x: x > 0.75
    np.random.seed(0)
    arr = np.random.random((100, 100))
    print(arr)

    tic = time.perf_counter()
    line_defs = line_definitions_for_array(arr, x, y, w, h, qualifier)
    toc = time.perf_counter()

    pprint.pprint(line_defs)
    print(toc-tic)


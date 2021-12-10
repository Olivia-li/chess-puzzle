import numpy as np
# Define all the shapes on the board
board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

l_shape = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1],
]

hat = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 2],
    [0, 0, 0, 2, 2, 2],
]

zig_zag = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 3, 3, 0, 0],
    [0, 0, 0, 3, 3, 3],
]

straight = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 4, 4, 4, 4, 4],
]

cross = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0],
    [0, 0, 0, 5, 5, 5],
    [0, 0, 0, 0, 5, 0],
]

t_shape = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0],
    [0, 0, 6, 6, 6, 6],
]

cube_ish = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 7, 7],
    [0, 0, 0, 0, 7, 7],
]


def num_empty_array(shape):
    count = 0
    for row in shape:
        if sum(row) == 0:
            count += 1
    return count

def rot90(shape):
    new_shape = np.rot90(shape)
    new_shape = np.roll(new_shape, num_empty_array(new_shape), axis=0)
    return new_shape


def fliplr(shape):
    shift_num = num_empty_array(np.rot90(shape))
    new_shape = np.fliplr(shape)
    new_shape = np.roll(new_shape, shift_num, axis=1)
    return new_shape

import numpy as np
import itertools

# ----- Board + Shape Generation -----
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
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
]

zig_zag = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
]

straight = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
]

cross = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
]

t_shape = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1],
]

cube_ish = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1],
]


# ----- Shape Generation Helper Functions -----
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

# ----- Data Type Conversions -----
def array_to_binary(shape):
    flat_shape = list(itertools.chain(*shape))
    string = ''.join(map(str, flat_shape))
    binary = int(string, 2)
    return binary

def binary_to_array(binary):
    string = format(binary, "b")
    string = (36-len(string)) * "0" + string
    array = []

    for i in range(6):
        temp = list(string[i*6:i*6+6])
        array.append(list(map(int, temp)))
    return array 

# ----- Validations -----
# Check if the shape is out of bounds by wrapping around the board
def is_out_of_bounds(shape):
    if len([i[0] for i in shape]) > 0 and len([i[5] for i in shape]) > 0:
        return True
    else:
        return False

# Check if the shape is overlapping with other shapes 
def has_overlap(board, shape):
    if board & shape > 0: # bitwise and
        return True
    else:
        return False

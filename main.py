import numpy as np
import itertools

COMPLETE_BOARD_NUM = 68719476735

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

def board_complete(board):
    # Find the bits that are not flipped on
    N = (~board & ~COMPLETE_BOARD_NUM) 
    # if N is a power of 2 there is only one bit not flipped on which means the puzzle is complete
    if N & N-1  == 0:
        return True
    else:
        return False

# ----- Shape Generation Helper Functions -----
def num_empty_rows(shape):
    count = 0
    for row in shape:
        if sum(row) == 0:
            count += 1
    return count

def num_empty_columns(shape):
    count = 0
    for i in range(0, 6):
        if sum([j[i] for j in shape]) == 0:
            count += 1
    return count

def rot90(shape):
    new_shape = np.rot90(shape)
    new_shape = np.roll(new_shape, num_empty_rows(new_shape), axis=0)
    return new_shape


def fliplr(shape):
    new_shape = np.fliplr(shape)
    new_shape = np.roll(new_shape, num_empty_columns(shape), axis=1)
    return new_shape

def generate_all_reflections_and_rotations(shape):
    shapes = []
    shapes.append(shape)
    shapes.append(rot90(shape))
    shapes.append(rot90(rot90(shape)))
    shapes.append(rot90(rot90(rot90(shape))))
    shapes.append(fliplr(shape))
    shapes.append(fliplr(rot90(shape)))
    shapes.append(fliplr(rot90(rot90(shape))))
    shapes.append(fliplr(rot90(rot90(rot90(shape)))))
    return shapes

# ------ Generate all Possible Shapes ------
def generate_shapes(shape):
    all_shapes = generate_all_reflections_and_rotations(shape)

    # Get rid of duplicates
    all_shapes = set(map(lambda x: array_to_binary(x), all_shapes))
    all_shapes = list(map(lambda x: binary_to_array(x), all_shapes))

    # Get rows and columns for each shape
    data = []
    for shape in all_shapes:
        data.append({"shape": array_to_binary(shape), "rows": num_empty_rows(shape), "columns": num_empty_columns(shape)})
    
    result = []
    for shape_data in data:
        for i in range(0, shape_data["rows"]+1):
            for j in range(0, shape_data["columns"]+1):
                result.append(shape_data["shape"] * (2**j) * (2**(6*i)))
    
    return result

def print_results(results):
    for result in results: 
        print(result)
    print("\n")

# ------ Main Function ------
def main():
    # Generate all possible shapes
    all_shapes = [cross]
    shape_combinations = []
    for shape in all_shapes:
        shape_combinations.append(generate_shapes(shape))

    for shape in shape_combinations:
        for result in shape:
            print_results(binary_to_array(result))
    result = []
    

# ------ Running the Program ------
main()

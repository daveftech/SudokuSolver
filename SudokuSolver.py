# VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# test_matrix = [
#     ['1','2','3','4','5','6','7','8','9'],
#     ['4','5','6','7','8','9','1','2','3'],
#     ['7','8','9','1','2','3','4','5','6'],
#     ['2','3','4','5','6','7','8','9','1'],
#     ['5','6','7','8','9','1','2','3','4'],
#     ['8','9','1','2','3','4','5','6','7'],
#     ['3','4','5','6','7','8','9','1','2'],
#     ['6','7','8','9','1','2','3','4','5'],
#     ['9','1','2','3','4','5','6','7','8']
# ]

init_cell_set = {'1','2','3','4','5','6','7','8','9'}

working_matrix = [
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ],
    [
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'},
        {'1','2','3','4','5','6','7','8','9'}
    ]
]

def print_grid(sudoku_matrix):
    if not is_matrix_valid(sudoku_matrix):
        return

    # Print header row
    print(u'\u2554' + u'\u2550' * 7 + u'\u2566' + u'\u2550' * 7 + u'\u2566' + u'\u2550' * 7 + u'\u2557')

    # Print first three rows
    print_row(sudoku_matrix[0])
    print_row(sudoku_matrix[1])
    print_row(sudoku_matrix[2])

    # Print separator row
    print(u'\u2560' + u'\u2550' * 7 + u'\u256C' + u'\u2550' * 7 + u'\u256C' + u'\u2550' * 7 + u'\u2563')

    # Print next three rows
    print_row(sudoku_matrix[3])
    print_row(sudoku_matrix[4])
    print_row(sudoku_matrix[5])

    # Print separator row
    print(u'\u2560' + u'\u2550' * 7 + u'\u256C' + u'\u2550' * 7 + u'\u256C' + u'\u2550' * 7 + u'\u2563')

    # Print last three rows
    print_row(sudoku_matrix[6])
    print_row(sudoku_matrix[7])
    print_row(sudoku_matrix[8])

    # Print footer row
    print(u'\u255A' + u'\u2550' * 7 + u'\u2569' + u'\u2550' * 7 + u'\u2569' + u'\u2550' * 7 + u'\u255D')

def print_row(row_list):
    if not is_row_valid(row_list):
        print('Row is not valid')
        return

    print(u'\u2551' + ' ' + row_list[0] + ' ' + row_list[1] + ' ' + row_list[2] + ' ' \
        + u'\u2551' + ' ' + row_list[3] + ' ' + row_list[4] + ' ' + row_list[5] + ' ' \
        + u'\u2551' + ' ' + row_list[6] + ' ' + row_list[7] + ' ' + row_list[8] + ' ' + u'\u2551')


def is_row_valid(row_list):
    return len(row_list) == 9

def is_matrix_valid(grid_matrix):
    if len(grid_matrix) != 9:
        return False

    for row in grid_matrix:
        if len(row) != 9:
            return False

    return True

def get_possible_values_for_row(grid_matrix, row, column):
    # Get the current row
    test_row = grid_matrix[row]

    # Check to see if the current cell is already set
    if test_row[column] != '0':
        return test_row[column]

    possible_values_set = set()

    for index, cell in enumerate(test_row):
        if index == column:
            continue

        if cell == '0':
            continue

        
    
print('Printing formated test matrix:')
print_grid(test_matrix)
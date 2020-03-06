# One list that holds x lists
# Create function that takes in 1 integer that defines the length of list and how many rows are in the matrix
# List starts at zero


def matrix_inc(num):
    my_list = []
    i = 0
    for _ in range(num):
        my_list.append(list(range(i, num)))
        i += 1
        num += 1
    return my_list


print(matrix_inc(5))

print('')
# Jordan's Solution


def manual_incrementing_matric(n):
    matrix = [[None for y in range(n)] for x in range(n)]

    counter = 0

    for idx, el in enumerate(matrix):
        for nested_idx, _ in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx

        counter += 1

    return matrix


print(manual_incrementing_matric(5))

print('')
# Instructor's solution


def manual_matrix(grid_area):
    matrix = []
    counter = 0

    while counter < grid_area:
        matrix.append(([x for x in range(counter, grid_area + counter)]))
        counter += 1
    return matrix


print(manual_matrix(5))

print('')


def matty_matrix(grid_area):
    starting_num = 0
    initial_matrix = grid_area
    matrix = []

    while starting_num != initial_matrix:
        matrix.append(list(range(starting_num, grid_area)))
        starting_num += 1
        grid_area += 1

    return matrix


print(matty_matrix(5))

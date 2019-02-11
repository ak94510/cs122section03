# ----------------------------------------------------------------------
# Name:        interest_calc
# Purpose:     A simple accrued interest calculator
#
# Date:       2/5/2019
# ----------------------------------------------------------------------
"""
Matrix manipulation functions

count the number of times a target appears in a matrix
gets adjacent coordinates given coordinate
blurs a image
"""

def count_matrix(matrix, target):
    """
    Counts the number of times target appears in matrix
    :param matrix: (list) list of lists of numbers
    :param target: (number) the number to count occurrences
    :return: (number) the number of occurrences of the target
    """
    total = 0
    for alist in matrix:
        for value in alist:
            if value is target:
                total = total + 1
    return total

def adjacent(matrix, target):
    """
    Returns the adjacent coordinates of the target in the matrix
    :param matrix: (matrix) list of list of numbers
    :param target: (tuple) the target to get adjacent coordinates
    :return: (set) the set of adjacent coordinates
    """
    x = target[0]
    y = target[1]
    total = {(x+x_index, y+y_index) for x_index in range(-1, 2)
             if len(matrix) > x+x_index > -1 for y_index in range(-1, 2)
             if len(matrix[0]) > y+y_index > -1}
    if target in total:
        total.remove(target)
    return total or None


def blur(matrix):
    """
    Blurs a image given lists of pixel colors
    :param matrix: (list) List of lists representing image to be blurred
    :return: (list) List of lists representing blurred image
    """
    returned = []
    for x in range(0, len(matrix)):
        row = []
        for y in range(0, len(matrix[0])):
            total = matrix[x][y]
            number_of_elements = 1
            for adjacent_coord in adjacent(matrix, (x, y)):
                total = total + \
                        matrix[adjacent_coord[0]][adjacent_coord[1]]
                number_of_elements += 1
            row.append(round(total/number_of_elements))
        returned.append(row)
    return returned


def main():
    image = [[168, 168, 170, 172, 174, 158, 154, 170],
             [172, 126, 109, 86, 72, 72, 95, 129],
             [146, 152, 165, 183, 176, 177, 178, 176],
             [181, 153, 80, 57, 79, 57, 29, 23],
             [29, 34, 19, 28, 38, 39, 15, 26],
             [14, 21, 18, 21, 21, 18, 24, 25]]
    print(blur(image))

if __name__ == "__main__":
    main()

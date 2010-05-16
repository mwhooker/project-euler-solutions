#!/usr/bin/python
import sys

"""
def reflected_y(grid):
    mirrored = list()
    for y in xrange(grid):
"""

def print_grid(grid):
    for y in grid:
        row = ""
        for x in y:
            row += "%s " % x
        sys.stderr.write(row)


def reflected_ll_ru(grid):
    rotated = list()
    for y in reversed(xrange(len(grid))):
        row = list()
        for x in reversed(xrange(len(grid[y]))):
            row.append(grid[x][y])
        rotated.append(row)

    return rotated

def reflected_ul_lr(grid):
    hlen = len(grid[0])
    vlen = len(grid)
    rotated = list()
    for y in xrange(vlen):
        rotated_row = list()
        for x in xrange(hlen):
            rotated_row.append(grid[x][y])
        rotated.append(rotated_row)
    return rotated

def read_in_file(file_name):
    grid = list()
    with open(file_name) as f:
        for line in f:
            grid.append(line.strip().split(' '))
    return grid

def product(array):
    return reduce(lambda x, y: int(x)*int(y), array)

def sum_rows(grid, n=4):
    results = list()
    for row in grid:
        for i in xrange((len(row) - n)):
            results.append(
                reduce(lambda x, y: int(x)*int(y),
                       row[i:(n+i)]
                      )
            )

    print_grid(grid)
    return results

def columns(grid, n=4):
    results = list()
    
    return sum_rows(reflected_ul_lr(grid))

def upper_left_diagonal(grid, n=4):
    results = list()
    vlen = len(grid)
    rotated = list()
    for y in xrange(vlen):
        rotated_row = list()
        for i in xrange(y+1):
            rotated_row.append(grid[y-i][i])
        rotated.append(rotated_row)
    
    return rotated

def diagonal_ll_to_ur(grid, n=4):
    diag = upper_left_diagonal(grid, n)
    diag2 = upper_left_diagonal(reflected_ll_ru(grid), n)
    return sum_rows(diag) + sum_rows(diag2)

def bottom_left_diagonal(grid, n=4):
    results = list()
    vlen = len(grid)
    rotated = list()
    for y in reversed(xrange(vlen)):
        rotated_row = list()
        for i in xrange(vlen-y):
            rotated_row.append(grid[y+i][i])
        rotated.append(rotated_row)
    
    return rotated

def diagonal_ul_to_lr(grid, n=4):
    diag = bottom_left_diagonal(grid, n)
    diag2 = bottom_left_diagonal(reflected_ul_lr(grid), n)
    return sum_rows(diag) + sum_rows(diag2)

def main():
    products = list()
    grid = read_in_file('grid.txt')
    print "Rows:"
    products.extend(sum_rows(grid))
    print "Columns:"
    products.extend(columns(grid))
    print "Diagonal ul->lr:"
    products.extend(diagonal_ul_to_lr(grid))
    print "Diagonal ll->ur:"
    products.extend(diagonal_ll_to_ur(grid))

    print max(products)


if __name__ == '__main__':
    exit(main())

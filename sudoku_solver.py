def can_place(mat, i, j, num, n):
    for k in range(n):
        if mat[i][k] == num or mat[k][j] == num:
            return False

    # check the submatrix
    sx = (i//3)*3
    sy = (j//3)*3
    for x in range(sx, sx+3):
        for y in range(sy, sy+3):
            if mat[x][y] == num:
                return False
    return True


def solve_sudoku(mat, i, j, n):
    # when all the cells are covered successfully
    if i == n:
        return True

    # after traversing all columns in a row forwarded to next row
    if j == n:
        return solve_sudoku(mat, i+1, 0, n)

    # if a number already put in this cell
    if mat[i][j]:
        return solve_sudoku(mat, i, j+1, n)
    else:
        for num in range(1, n+1):
            if can_place(mat, i, j, num, n):
                mat[i][j] = num
                if solve_sudoku(mat, i, j+1, n):
                    return True
        mat[i][j] = 0
        return False

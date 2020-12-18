# https://www.interviewbit.com/problems/valid-sudoku/

size = 9


def rowIsOk(board, row):
    arr = [0] * size
    for elem in board[row]:
        if elem != ".":
            arr[int(elem) - 1] += 1
            if arr[int(elem) - 1] > 1:
                return False
    return True
    
    
def colIsOk(board, col):
    arr = [0] * size
    for i in range(size):
        elem = board[i][col]
        if elem != ".":
            arr[int(elem) - 1] += 1
            if arr[int(elem) - 1] > 1:
                return False
    return True


def blockIsOk(board, row, col):
    arr = [0] * size
    row = (row // 3) * 3
    col = (col // 3) * 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            elem = board[i][j]
            if elem != ".":
                arr[int(elem) - 1] += 1
                if arr[int(elem) - 1] > 1:
                    return False
    return True


def isOk(board, r, c):
    return rowIsOk(board, r) and colIsOk(board, c) and blockIsOk(board, r, c)


def solve(board, row, col):
    if row == size:
        return True
    if board[row][col] == ".":
        oldStr = board[row]
        for num in range(1, size + 1):
            newStr = oldStr[:col] + str(num) + oldStr[col + 1:]
            board[row] = newStr
            if isOk(board, row, col):
                res = False
                if col == size - 1:
                    res = solve(board, row + 1, 0)
                else:
                    res = solve(board, row, col + 1)
                if res:
                    return True
        board[row] = oldStr
    else:
        if col == size - 1:
            return solve(board, row + 1, 0)
        else:
            return solve(board, row, col + 1)
    return False


class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        board = list(A)
        for r in range(size):
            for c in range(size):
                if not isOk(board, r, c):
                    return 0
        if solve(board, 0, 0):
            return 1
        else:
            return 0

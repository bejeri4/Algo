# https://www.interviewbit.com/problems/nqueens/
# Python 2.7

import copy

def getEmptyBoardWithSize(n):
    result = []
    for _ in range(n):
        result.append("." * n)
    return result
    
    
def checkDiag(n, board, row, col, rV, cV):
    while row >= 0 and row < n and col >= 0 and col < n:
        if board[row][col] == "Q":
            return False
        row += rV
        col += cV
    return True
    
    
def isOkToPlace(n, board, row, col):
    for i in range(n):
        if board[i][col] == "Q":
            return False
    return checkDiag(n, board, row, col, 1, 1) and checkDiag(n, board, row, col, 1, -1) and checkDiag(n, board, row, col, -1, 1) and checkDiag(n, board, row, col, -1, -1)


def place(board, row, col):
    rowStr = board[row]
    rowStr = rowStr[:col] + "Q" + rowStr[col + 1:]
    board[row] = rowStr


def remove(board, row, col):
    rowStr = board[row]
    rowStr = rowStr[:col] + "." + rowStr[col + 1:]
    board[row] = rowStr

    
def generate(n, row, soFar, result):
    if row == n:
        result.append(copy.copy(soFar))
        return
    for col in range(n):
        if isOkToPlace(n, soFar, row, col):
            place(soFar, row, col)
            generate(n, row + 1, soFar, result)
            remove(soFar, row, col)


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        if A == 0:
            return []
        result = []
        soFar = getEmptyBoardWithSize(A)
        generate(A, 0, soFar, result)
        return result

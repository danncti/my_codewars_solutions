#!/usr/bin/env python3

from re import findall

def done_or_not(board):
    if not dup_row(board, 9): return 'Try again!'
    if not dup_col(board, 9): return 'Try again!'
    if not check_reg(board, 9): return 'Try again!'
    return 'Finished!'

def dup_row(board, n):
    x = []
    for a in board:
        x.append(''.join(str(e) for e in a))
        if not check_dup(x[-1], n): return False
    x = set(x)
    return len(x) == n

def dup_col(board, n):
    return dup_row(list(map(list, zip(*board))), n)

def check_dup(reg, n):
    if len(set(findall("[0-9]", reg))) != n: return False
    return True

def check_reg(board, n):
    a = []
    for i in range(n):
        a.append([0] * n)

    x = 0
    y = 0
    for i in range(n):
        for ii in range(n):
            a[((i // 3) * 3) + (ii // 3)][x + y] = board[i][ii]
            y += 1
            if y > 2: y = 0
        x += 3
        if x > 6: x = 0
    for ch in a:
        if not check_dup(''.join(str(x) for x in ch), n): return False
    return True
import numpy as np

def valid_solution(board):  # board[i][j]
    newb = np.array(board)

    # rows = [newb[x, :] for x in range(9)]
    cols = [newb[:, y] for y in range(9)]
    # sqrs = [board[x:x + 3, y:y + 3].flatten() for x in [0, 3, 6] for y in [0, 3, 6]]

    sqrs = []
    for x in [0, 3, 6]:
        for y in [0, 3, 6]:
            sqrs.append(newb[x:x + 3, y:y + 3].flatten())

    for lines in np.vstack((board, cols, sqrs)):
        if len(np.unique(lines)) != 9 or 0 in lines:
            return False


    return True



# below - not in the answer
def main():
    # print("ord", order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
    # assert order_weight("12 31 105 24 6 60 43 7 7 107 117 9 163 173 182 47 83 183 192 192 84 157 175 167 185 159 152080 28015 28015 28015 424116 434530 73406 107924 439043 379033 401929 206459 454454 481328 315369 436168 18983 370955 371558 439904 172974 490926 90993 297536 390938") == "12 31 105 24 6 60 43 7 7 70 107 117 9 163 173 182 47 83 183 192 84 93 157 175 167 185 159 152080 28015 2860 406015 424116 434530 73406 107924 439043 379033 401929 206459 454454 481328 315369 436168 18983 370955 371558 439904 172974 490926 90993 297536 390938"
    assert valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True


if __name__ == "__main__":
    main()
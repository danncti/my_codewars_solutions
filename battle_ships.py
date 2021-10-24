def damaged_or_sunk(board, attacks):
    res = {'sunk': 0, 'damaged': 0, 'not_touched': 0, 'points': 0}
    at = []
    bl = len(board)

    for hit in attacks:
        t = board[bl - hit[1]][hit[0]-1]
        board[bl - hit[1]][hit[0] - 1] = 0
        if t != 0 and t not in at:
            at.append(t)
    for a in at:
        if not any(a in x for x in board):
            res['sunk'] += 1
        if any(a in x for x in board):
            res['damaged'] += 1
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y] == a:
                        board[x][y] = 0
    temp = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != 0:
                if board[x][y] not in temp:
                    temp.append(board[x][y])
                    board[x][y] = 0

    res['not_touched'] = len(temp)

    res['points'] = (res['sunk']) + (res['damaged'] * 0.5) + (res['not_touched'] * -1)

    return res



# below - not in the answer
def main():
    board = [[0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 0]]

    attacks = [[3, 1], [3, 2], [3, 3]]

    assert damaged_or_sunk(board, attacks) == { 'sunk': 1, 'damaged': 0 , 'not_touched': 0, 'points': 1}

    # board = [[3, 0, 1],
    #          [3, 0, 1],
    #          [0, 2, 1],
    #          [0, 2, 0]]
    #
    # attacks = [[2, 1], [2, 2], [ 3, 2], [3, 3]]
    #
    # assert damaged_or_sunk(board, attacks) == { 'sunk': 1, 'damaged': 0 , 'not_touched': 0, 'points': 1}



if __name__ == "__main__":
    main()
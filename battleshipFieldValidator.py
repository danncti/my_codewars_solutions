def validate_battlefield(field):
    positions=[]
    for x in range(10):
        for y in range(10):
            if field[x][y] == 1:
                positions.append([x, y])
    if len(positions) != 20: return False

    connected = [['']*4 for _ in range(10)]
    no = 0
    added = 1
    for x in range(20):
        a = positions[x]
        l = 0
        xx = False
        yy = False
        newLineFirst = True
        nextLine = False
        xlast = 0
        ylast = 0

        firstAdded = False
        if x == 0:
            connected[no][l] = a
            xlast = a[0]
            ylast = a[1]
            l += 1
            firstAdded = True
        for y in range(1, 20):
            justAdded = False
            b = positions[y]
            find = find2(connected, b)
            if find: continue
            if a[0] + l == b[0] and a[1] == b[1] or ( a[1]+1 == b[1] and xx == True and b[0] == xlast):
                if a[1] + 1 == b[1] and not newLineFirst:
                        return False
                if yy != False:
                    if a[1] + 1 == b[1]:
                        return False
                    continue
                if not newLineFirst:
                    xx = True
                if l > 3: return False
                connected[no][l] = b
                justAdded = True
                xlast = b[0]
                l += 1
                newLineFirst = False
                nextLine = True
                added += 1
                pass
            if a[1] + l == b[1] and a[0] == b[0] or  (a[0] + 1 == b[0] and xx == True and b[1] == ylast):
                if justAdded: continue
                if a[0] + 1 == b[0] and not newLineFirst:
                    return False
                if xx != False:
                    if a[0] + 1 == b[1]:
                        return False
                    continue

                if not newLineFirst:
                    yy = True
                if l > 3: return False
                connected[no][l] = b
                ylast = b[1]
                l += 1
                newLineFirst = False
                nextLine = True
                added += 1
                pass

        if nextLine or firstAdded: no += 1

    test = check_diag(connected)
    if test: return False
    test = check_long(connected)
    if not test: return False

    return True


def find2(searchList, elem):

    for line in searchList:
        for value in line:
            if elem == value:
                return True
    return False

def check_diag(positions):

    for x in range(10):
        for y in range(4):
            a = positions[x][y]
            if type(a) == list:
                xx = a[0]
                yy = a[1]
                if xx > 0:
                    if find2(positions, [xx -1, yy+1]): return True
                if xx <9:
                    if find2(positions, [xx + 1, yy + 1]): return True
    return False

def check_long(positions):
    table = []
    for x in range(10):
        counter = 0
        for y in range(4):
            a = positions[x][y]
            if type(a) == list:
                counter += 1
        table.append(counter)
    table = sorted(table)
    for x in [4, 3,3, 2,2,2, 1,1,1,1]:
        if x in table:
            table.remove(x)
        else: return False
    return True

# below - not in the answer - not my code
def validateBattlefield(field):
    B, F = {(r, c) for c in range(10) for r in range(10) if field[r][c]}, {}

    def touching(r, c):
        B.discard((r, c))
        P = {(r, c)} | {n for p in {(r + rr, c + cc) for rr in [-1, 0, 1] for cc in [-1, 0, 1]} & B for n in
                        touching(*p)}
        return [] if len(set(r for r, _ in P)) > 1 and len(set(c for _, c in P)) > 1 else P

    while B:
        ship = len(touching(*B.pop()))
        F[ship] = F.get(ship, 0) + 1
    return F == {4: 1, 3: 2, 2: 3, 1: 4}

def main():

    battleField = [[1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    assert validateBattlefield(battleField) == True

    # battleField = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    #                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    #                 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #                 [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    #                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    #                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    #                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    #                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
    # assert validate_battlefield(battleField) == True

    # battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    #                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    #                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    #                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    # assert validate_battlefield(battleField) == False
    #
    # battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    #                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    #                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    #                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    #                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    # assert validate_battlefield(battleField) == True

    battleField =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]
    assert validate_battlefield(battleField) == True

    # battleField =  [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    #                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    #                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    #                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # assert validate_battlefield(battleField) == True

if __name__ == "__main__":
    main()
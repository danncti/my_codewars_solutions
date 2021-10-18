def next_bigger(n):
    res = [int(x) for x in str(n)]
    last = res[-1:][0]
    changed = False
    new =[]
    changedPos = 0
    temp= 1

    for i in reversed(res[:-1]):
        temp +=1
        if i < last and not changed:
            changed = True
            changedPos = temp
        new.insert(0, last)
        last = i

    new.insert(0, last)
    if not changed: return -1
    return(int(''.join(str(e) for e in second(new, changedPos))))

def second(n, x):

    toSort = n[-x:]
    toChange = sorted([i for i in n[-x+1:] if i > int(n[-x:-x+1][0]) ])[0]
    toSort.remove(toChange)
    new = n[:-x]
    new.append(toChange)
    new = new + sorted(toSort)
    return new


# below - not in the answer
def main():

    # assert next_bigger(12234) == 12243
    # assert next_bigger(12341) == 12431
    assert next_bigger(9876543210) == -1
    assert next_bigger(59884848459853) == 59884848483559

if __name__ == "__main__":
    main()

def next_smaller(n):

    dList = list(str(n))
    for pos, d in reversed(tuple(enumerate(dList))):
        toCheck = dList[pos:]
        if d > min(toCheck):
            first, firstPos = max((v, p) for p, v in enumerate(toCheck) if v < d)
            del toCheck[firstPos]
            dList[pos:] = [first] + sorted(toCheck, reverse=True)
            if dList[0] == '0':return -1
            return int(''.join(dList))
    return -1



def main():
    assert(next_smaller(51226262651257)) == 51226262627551

if __name__ == "__main__":
    main()


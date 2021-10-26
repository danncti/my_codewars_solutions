class SubSet:

    def __init__(self):
        self.results = []
        self.toRet = False

    def subset_sum(self, numbers, target, partial=[]):

        s = sum(partial)
        if s > target:
            return

        if s == target:
            self.results.append(partial)
            return

        la = len(self.results)
        if la > 1:
            for l in range(min(len(self.results[la-2]), len(self.results[la-1]))):
                if sum(self.results[la-2][l:]) > sum(self.results[la-1][l:]):
                    self.results.remove(self.results[la-2])
                    self.toRet = True
                    break
                else:
                    self.results.remove(self.results[la-1])
                    self.toRet = True
                    break
        elif la == 1:
            if self.results[0][0] > partial[0]:
                self.toRet = True
                return self.toRet

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i + 1:]
            if self.toRet: return
            if self.subset_sum(remaining, target, partial + [n]): break
        return self.toRet

def decompose(n):
    n1 = n - 1
    n2 = n**2
    list2 = []

    while(n1 >= 1):

        s = n1**2
        n2 = n2 - s
        if(n1>2999):
            n1 = int(n2**(1/2)+1)
        list2.append(s)
        n1 -= 1

    subset = SubSet()
    subset.subset_sum(list2, n**2)
    if len(subset.results) == 0:
        return None

    ret = []
    for x in subset.results:
        for y in x:
            ret.append(int(y**(1/2)))
    ret = sorted(ret)
    return ret

# not mine solution
def decomposeNM(n, a=None):
    if a == None: a = n*n
    if a == 0: return []
    for m in range(min(n-1, int(a ** .5)), 0, -1):
        sub = decomposeNM(m, a - m*m)
        if sub != None: return sub + [m]

# below - not in the answer
def main():
    # decompose(1234567)
    # decompose(8)
    # dec(44)
    assert decomposeNM(117138) == [5, 31, 483, 117137]
    # assert decompose(850947) == [1, 6, 12, 36, 1304, 850946]
    # assert decompose(1234567) == [2, 8, 32, 1571, 1234566]
    # assert decompose(50) == [1, 3, 5, 8, 49]
    # assert decompose(12) == [1, 2, 3, 7, 9]
    # assert decompose(8) == None


if __name__ == "__main__":
        main()
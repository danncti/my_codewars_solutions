def unique_in_order(iterable):
    new = []
    for x, e in enumerate(iterable):
        if(x):
            if new[-1] != e: new.append(e)
        else: new.append(e)
    # print(new)
    return new

def unique_in_order2(iterable):
    new = []
    for x, e in enumerate(iterable):
        new[-1] != e and new.append(e) if(x) else new.append(e)
    return new

import time

def main():
    tests = 100000
    start_time = time.time()
    for a in range(tests):
        assert(unique_in_order('AAAABBBCCDAABBB')) == ['A','B','C','D','A','B']
        assert(unique_in_order([1,2,2,3,3])) == [1,2,3]

    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    for a in range(tests):
        assert (unique_in_order2('AAAABBBCCDAABBB')) == ['A', 'B', 'C', 'D', 'A', 'B']
        assert (unique_in_order2([1, 2, 2, 3, 3])) == [1, 2, 3]

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
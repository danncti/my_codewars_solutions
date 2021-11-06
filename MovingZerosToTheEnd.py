
def move_zeros(array):
    z = 0
    for x in range(len(array)):
        if(array[x-z] == 0):
            del array[x-z]
            z += 1
    if(z): return array + [0]*z
    return array

def move_zeros1(array):
    z = 0
    new = []
    # for x, a in enumerate(array):
    for x in range(len(array)):
        if(array[x] != 0):
            new.append(array[x])
        else: z += 1
    if(z): return new + [0]*z
    return array


import time

def main():
    tests = 10000
    start_time = time.time()
    for a in range(tests):
        assert(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    for a in range(tests):
        assert(move_zeros1([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
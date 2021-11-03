def find_outlier(integers):
    l = 0
    for i in range(3):
        if(integers[i]%2): l-=1
        else: l +=1

    if(l>0): # find odd
        for i in integers:
            if(i%2): return i
    else:
        for i in integers:
            if(i%2==0): return i
    return None

import time
def main():
    tests = 1

    start_time = time.time()
    for a in range(tests):
        assert (find_outlier([2, 4, 6, 8, 10, 3])) == 3
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

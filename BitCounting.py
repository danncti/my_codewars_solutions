def count_bits(n):
    b = "{0:b}".format(n)
    return b.count('1')



import time

def main():

    tests = 1
    start_time = time.time()
    for a in range(tests):
        count_bits(10)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
        main()
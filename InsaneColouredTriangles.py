import time

def conv_base_3( n, out):
    i = 0
    for i in range(11):
        if (n <= 0): break
        out.append(int(n % 3))
        n = int( n / 3)
    return i

# def conv_base_3( n, out):
#     i = 0
#     for i in range(11):
#         if (n <= 0): break
#         out[i] = int(n % 3)
#         n = int( n / 3)
#     return i

def lucas_3(len_n, dig_n, len_k, dig_k):
    prod = 1
    for i in range(len_n):
    # for (unsigned i = 0; i < len_n; i++) {
        n_i = dig_n[i]
        if(i < len_k):
            k_i = dig_k[i]
        else:
            k_i = 0
        prod = (prod * binom_max_2(n_i, k_i)) % 3
    return prod % 3

# // calculate the binomial coefficient for n < 3
def binom_max_2( n,  k):
    if (n < k): return 0
    if(n == 0 or n ==1): return 1
    elif (n == 2): return 1 + (k == 1)

def triangle(row):
    start_time = time.time()
    # if(len(row)>51000):
#         return
    cti = {"R": 0, "G": 1, "B": 2}
    itc = {0: "R", 1: "G", 2: "B"}
    sum = 0
    n = len(row)
    dig_n = []
    len_n = conv_base_3(n - 1, dig_n)

    for km1 in range(n):
        dig_k =  []
        len_k = conv_base_3(km1, dig_k)

        Cnk_mod3 = lucas_3(len_n, dig_n, len_k, dig_k)

        sum = (sum + Cnk_mod3 * cti[row[km1]]) % 3

    sign = (n % 2) * 2 - 1
    sum_mod3 = (3 + (sign * (int)(sum % 3))) % 3

    # print(len(row), "--- %s seconds ---" % (time.time() - start_time))
    # print(itc[sum_mod3])
    # return ''.join('RGB'[sum_mod3])
    return itc[sum_mod3]

def trianglea(row):
    r = list(row)
    print(len(row))
    col= {"G": 0, "B":1, "R":2}
    c = {0:"G" ,1:"B" ,2: "R"}
    l = 0
    while len(r) > 1:
        l = len(r) -1
        for x in range(l):
            a = col[r[x]]
            b = col[r[x + 1]]
            if (a != b):
                r[x] = (c[3-(a + b)])
        del r[-1]
    return r[0]


def main():
    # https://stackoverflow.com/questions/53585022/three-colors-triangles
    tests = 10

    start_time = time.time()
    for a in range(tests):
        assert (triangle('BBRBBGRBRRGBRGRBGRRBBGRGGGGBGGBRGBGRRBGGBGBRGBBBRRBBBBRRBRBBBRGBRRBBRRGGBGGGRGBRRGRGGGRBGGBGGBGRBBRGRBRBGGBRRBRRRGGRGRRRRRGRRGBBRGBBBGGBRRRRBRRRRBGRRGGBRBBGRGBRBGGBRBRGBGBGBGRBRGRBBRRRBRBRRGBBRRGGRRGRBRRGRBRBGRRRGRRGGBBRGGRGBRBBBRGRBGGGBRBBGBBRRRRGGBGRRGGGBBBBRRBRGRBRGGGBBBGBBGGRGRBGRRBGGGBGBGRBGGRGBBRRGBRGRRBRGGBRGBGGGRGRBRBGRRBBRBGBBGBGBGRGGRRBGGRBBRRGGGBBBRBBBBRGBRGGBBBBGRBRBGBBRGGRRRRBBBGGGBBRGGGRGGBGGBRRBBRRRBBRGBRGBRBGGRRGGBBRGRGBGBGBBBBRGBGGRRGRGRGBBRBGRGGGRBRBRGGRGRGRBGBRGGBBGRGGBRBGBGGGBGBRBBRGGGBBRRRBRRRGBRBBGRGGBRBRGBGRRBRRBRBGGGGRRGRBRRBBGGRRBBBGBGGBRGGGBRRRBRGRBRBBGRBGRBBRGGRGRBRBBGGRRBGRRGRRRBRRBGGRRRBRRBBRBBRRGGBBRRBGBBGGRRGRRGGRGBBGGGGGRBBGRGGGRRGRBGGGGGRBRRRRGRGRRRRBGBBBBRRRGBRBGGBBGBGBBGGBBGBGGBBGGBGRRRRGBBGRRRGBGBBRGGRGRGRGBBBBGRRBRRRGRBRBRBGBGGBBBG')) == 'G'
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

import re

def order_weight(strng):

    t = strng.split()
    x = []
    for n in t:
        x.append([n, sum_digits(int(re.findall(r'\d+', n)[0]))])

    x = sorted(x, key=lambda a: a[1])

    return sortx(x)

def sortx(x):
    new = [0] * len(x)
    i = 0
    added2 = False
    for a, b in zip(x, x[1:]):
        if i ==0:
            new[i] = a
        if a[1] == b[1] and added2 == False:
            if a[0] > b[0]:
                new[i] = b
                new[i + 1] = a
                added2 = True
            else:
                new[i + 1] = b
        else:
            new[i+1] = b
        i += 1

    if added2:
        return sortx(new)
    else:
        new2 = []
        for n in x:
            new2.append(n[0])

        return ' '.join(new2)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


# below - not in the answer
def main():
    # print("ord", order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
    # assert order_weight("12 31 105 24 6 60 43 7 7 107 117 9 163 173 182 47 83 183 192 192 84 157 175 167 185 159 152080 28015 28015 28015 424116 434530 73406 107924 439043 379033 401929 206459 454454 481328 315369 436168 18983 370955 371558 439904 172974 490926 90993 297536 390938") == "12 31 105 24 6 60 43 7 7 70 107 117 9 163 173 182 47 83 183 192 84 93 157 175 167 185 159 152080 28015 2860 406015 424116 434530 73406 107924 439043 379033 401929 206459 454454 481328 315369 436168 18983 370955 371558 439904 172974 490926 90993 297536 390938"
    assert order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99"
    assert order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") == "11 11 2000 10003 22 123 1234000 44444444 9999"
    assert order_weight("") == ""


if __name__ == "__main__":
    main()
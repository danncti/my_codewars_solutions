#!/usr/bin/env python3
def productFib(prod):
    n1, n2 = 0, 1

    while n1 * n2 <= prod:

        if (n1 * n2) == prod:
            return [n1, n2, True]
        nth = n1 + n2
        n1 = n2
        n2 = nth

    return [n1, n2, False]

# below - not in the answer
def main():

    assert productFib(4895) == [55, 89, True]
    assert productFib(4899) == [89, 144, False]

if __name__ == "__main__":
    main()

import itertools


def subset_sum(numbers, target, partial=[], table=[]):
    s = sum(partial)
    z = len(table)
    if len(table) > 3:
        for t in range(len(table) - 1):
            if table[0][0+t] > table[1][0+t]:
                # print(table[0])
                return table[0]
            elif table[0][0+t] < table[1][0+t]:
                # print(table[0])
                return table[1]

        return
    # check if the partial sum is equals to target
    if s == target:
        # if len(table) > 3:
        #     return
        table.append(partial)
        print ( "sum(%s)=%s" % (partial, target))
        # return ( "sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n], table)

def decompose(n):
    n1 = n - 1
    n2 = n **2

    print("n, n2", n, n2)
    temp = []
    list2 = []
    while(n1 >= 1):
        s = n1**2
        # if x%1 == 0:
        temp.append([n1, s])
        list2.append(s)
        # print("n3, x", n1, s)
        n1 -= 1

    newa = subset_sum(list2, n2)
    print(list2)
    print(newa)
    return


# below - not in the answer
def main():
    decompose(50)
    # dec(44)
    # assert decompose(44) == [2, 3, 5, 7, 43]
    # assert decompose(50) == [1, 3, 5, 8, 49]
    # assert decompose(12) == [1, 2, 3, 7, 9]
    # assert decompose(8) == None


if __name__ == "__main__":
        main()

#         import itertools
#
#
# def subset_sum(numbers, target, partial=[], table=[]):
#     s = sum(partial)
#     if len(table) > 3: return
#     # check if the partial sum is equals to target
#     if s == target:
#         # table.append(partial)
#         if len(table) > 3:return
#         table.append(partial)
#         print ( "sum(%s)=%s" % (partial, target))
#     if s >= target:
#
#         return  # if we reach the number why bother to continue
#
#     for i in range(len(numbers)):
#         n = numbers[i]
#         remaining = numbers[i + 1:]
#         subset_sum(remaining, target, partial + [n], table)
#
# def subset_sum2(numbers, target, partial=[], partial_sum=0):
#     if partial_sum == target:
#         yield partial
#     if partial_sum >= target:
#         return
#     for i, n in enumerate(numbers):
#         remaining = numbers[i + 1:]
#         yield from subset_sum2(remaining, target, partial + [n], partial_sum + n)
#
# def dec(n):
#     n1 = n - 1
#     n2 = n ** 2
#
#     print("n, n2", n, n2)
#     temp = []
#     numbers = []
#     while (n1 >= 1):
#         s = n1 ** 2
#         # if x%1 == 0:
#         temp.append([n1, s])
#         numbers.append(s)
#         # print("n3, x", n1, s)
#         n1 -= 1
#
#     # print(list2)
#     print("start")
#     # numbers = [1, 2, 3, 7, 7, 9, 10]
#     result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == n2]
#     print(result)
#
# def decompose(n):
#     n1 = n - 1
#     n2 = n **2
#
#     print("n, n2", n, n2)
#     temp = []
#     list2 = []
#     while(n1 >= 1):
#         s = n1**2
#         # if x%1 == 0:
#         temp.append([n1, s])
#         list2.append(s)
#         # print("n3, x", n1, s)
#         n1 -= 1
#
#     new = subset_sum(list2, n2)
#     print(list2)
#     return
#     # result = [seq for i in range(len(list2), 0, -1) for seq in itertools.combinations(list2, i) if sum(seq) == n ** 2]
#     #
#     # print(result)
#     # return
#
#     sqr = []
#     couunter = 0
#     position = 0
#     # print("temp", temp)
#     # print("temp l", len(temp))
#     sum = 0
#     sum_no = 0
#     for x, s in reversed(temp):
#         # print("temp n1, n12", x, s)
#         if sum < n2:
#             sum += s
#             sum_no += 1
#
#     print("elements ", sum_no)
#         # if couunter + s
#     sum_no = len(temp) - sum_no
#
#
#     print(len(temp))
#     froe = 0
#     no = 0
#     for a in range(len(temp)):
#         sqr.append([])
#         couunter = 0
#         tempPos = position
#
#         print("a", a)
#         tr = temp
#         temp2 = temp
#         tr_pos = -1
#         for xs in tr:
#             x, s = xs
#             # print("temp n1, n12", x, s)
#             # if couunter + s
#             tr_pos +=1
#             if couunter < n2 and couunter + s <= n2:
#                 if tempPos > 0 and couunter > 0:
#                     tempPos -= 1
#                     continue
#                 print("+++  n1, n12", x, s)
#                 couunter += s
#                 sqr[no].append(x)
#             else:
#                 temp2.remove([x,s])
#         # print("count",couunter, n2)
#
#         if couunter == n2:
#             no += 1
#             if(len(sqr) > 25): break
#             pass
#         else:
#             print(sqr)
#             sqr.pop()
#             print(sqr)
#
#         position += 1
#         if position >= sum_no:
#             froe+=1
#             position = 0
#         if froe > sum_no: break
#
#     if couunter != n2:
#         print("none")
#         return None
#
#     # sqr.sort()
#     print(sqr)
#     return sqr
#
# # below - not in the answer
# def main():
#     decompose(50)
#     # dec(44)
#     # assert decompose(44) == [2, 3, 5, 7, 43]
#     # assert decompose(50) == [1, 3, 5, 8, 49]
#     # assert decompose(12) == [1, 2, 3, 7, 9]
#     # assert decompose(8) == None
#
#
# if __name__ == "__main__":
#         main()
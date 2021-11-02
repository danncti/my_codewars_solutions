def matrix_mult(a, b):
    result = [[0 for value in row] for row in a]
    for x in range(len(a)):
       for y in range(len(b[0])):
            for z in range(len(b)):
                result[x][y] += a[x][z] * b[z][y]
    return result

def matrix_mult2(a, b):
    return [[sum(a[x][z]*b[z][y] for z in range(len(a))) for y in range(len(a))] for x in range(len(a))]

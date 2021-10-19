def move_zeros(array):
    l = len(array)
    array = list(filter(lambda a: a != 0, array))
    array.extend([0] * (l - len(array)))

    return(array)

def move_zeros_old_sollution(array):
    if len(array)<2:
        return array
    new = []
    last = -1
    zeros = 0
    for a, b in zip(array, array[1:]):
        if a == 0:
            zeros += 1
        else:
            new.append(a)
        last = b
    if last != -1:
        new.append(last)
    if zeros > 0:
        new.extend([0] * zeros)

    return new

# below - not in the answer
def main():

    assert move_zeros2([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros2([0, 0]) == [0]

if __name__ == "__main__":
    main()

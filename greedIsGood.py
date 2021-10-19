def score(dice):
    points = 0

    if dice.count(2) >= 3: points += 200
    if dice.count(3) >= 3: points += 300
    if dice.count(4) >= 3: points += 400
    if dice.count(6) >= 3: points += 600

    n = dice.count(1)
    if n >= 3:
        points += 1000
        n -= 3
    points += (n * 100)

    n = dice.count(5)
    if n >= 3:
        points += 500
        n -= 3
    points += (n * 50)

    return points

# below - not in the answer
def main():
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4,  4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450

if __name__ == "__main__":
    main()
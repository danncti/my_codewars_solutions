def cakes(recipe, available):
    max = -1
    cur = 0
    for r in recipe:
        if not r in available: return 0
        cur = int(available[r]/recipe[r])
        if cur < 1: return 0
        if max == -1:
            max = cur
        if cur < max:
            max = cur
    return max


# below - not in the answer
def main():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    cakes(recipe, available)
    assert cakes(recipe, available) == 2

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}

    cakes(recipe, available)

    assert cakes(recipe, available) == 0

if __name__ == "__main__":
    main()

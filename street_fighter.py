def street_fighter_selection(fighters, initial_position, moves):

    l = len(fighters[0]) -1
    lx = len(fighters) - 1
    ip = list(initial_position)
    ret = []

    m = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

    for step in moves:
        x , y = m[step]
        ip[0] += x
        ip[1] += y

        if ip[0] < 0: ip[0] = 0
        elif ip[0] > lx: ip[0] = lx

        if ip[1] > l: ip[1] = 0
        elif ip[1] < 0: ip[1] = l

        ret.append( fighters[ip[0]][ip[1]] )
    return ret

# below - not in the answer
def main():

    fighters = [
        ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]

    moves = ["left"] * 8
    solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']

    assert street_fighter_selection(fighters, (0, 0), moves) == solution

if __name__ == "__main__":
    main()
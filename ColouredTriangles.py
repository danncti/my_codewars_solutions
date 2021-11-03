def triangle(row):
    if(len(row)<=1): return row
    new = ''
    for a in range(len(row)-1):
        col = "GBR"
        if (row[a] == row[a+1]): new += row[a]
        else:
            col = col.replace(row[a],'')
            col = col.replace(row[a+1],'')
            new += col
    return triangle(new)

def main():
    # assert(triangle('GB')) =='R'
    # assert(triangle('G')) =='G'
    assert(triangle('RBRGBRBGGRRRBGBBBGG')) =='G'

if __name__ == "__main__":
    main()

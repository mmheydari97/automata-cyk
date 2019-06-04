def create_cell(first, second):
    res = set()
    for f in first:
        for s in second:
            res.add(f+s)
    return res


length = 7


def cyk_alg():
    table = [[set() for _ in range(length-i)] for i in range(length)]
    for i, cell in enumerate(table[0]):
        cell.add(chr(65+i))
    print(table)


if __name__ == '__main__':
    cyk_alg()

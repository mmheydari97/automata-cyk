import os


def create_cell(first, second):
    res = set()
    if first == set() or second == set():
        return set()
    for f in first:
        for s in second:
            res.add(f+s)
    return res


def read_grammar(filename="./grammar.txt"):
    filename = os.path.join(os.curdir, filename)
    with open(filename) as grammar:
        rules = grammar.readlines()
        variables = []
        terminals = []

        for rule in rules:
            left, right = rule.split(" -> ")
            right = right[:-1].split(" | ")
            for r in right:
                if str.islower(r):
                    terminals.append([left, r])
                else:
                    variables.append([left, r])

        return variables, terminals


def read_input(filename="./input.txt"):
    filename = os.path.join(os.curdir, filename)
    res = []
    with open(filename) as inp:
        inputs = inp.readlines()
        for i in inputs:
            res.append(i[:-1])
    return res


def cyk_alg(varies, terms, inp):
    length = len(inp)
    var0 = [va[0] for va in varies]
    var1 = [va[1] for va in varies]
    table = [[set() for _ in range(length-i)] for i in range(length)]

    # Deal with variables
    for i, cell in enumerate(table[0]):

        for te in terms:
            if inp[i] == te[1]:
                table[0][i].add(te[0])

    # Deal with terminals
    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                row = create_cell(table[k][j], table[i-k-1][j+k+1])
                for ro in row:
                    if ro in var1:
                        table[i][j].add(var0[var1.index(ro)])
    for row in table:
        print(row)


if __name__ == '__main__':
    v, t = read_grammar()
    r = read_input()
    cyk_alg(v, t, "aaabbbcc")

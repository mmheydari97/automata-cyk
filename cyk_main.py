import os
from builtins import print


def create_cell(first, second):
    res = set()
    for f in first:
        for s in second:
            res.add(f+s)
    return res


def read_grammar(filename="./grammar.txt"):
    filename = os.path.join(os.curdir, filename)
    with open(filename) as grammar:
        rules = grammar.readlines()
        rights = []
        lefts = []

        for rule in rules:
            left, right = rule.split(" -> ")
            right = right[:-1].split(" | ")
            lefts.append(left)
            rights.append(right)

        return lefts, rights


def read_input(filename="./input.txt"):
    filename = os.path.join(os.curdir, filename)
    res = []
    with open(filename) as inp:
        inputs = inp.readlines()
        for i in inputs:
            res.append(i[:-1])
    return res


def cyk_alg(V, T, inp):
    length = len(inp)

    table = [[set() for _ in range(length-i)] for i in range(length)]

    # Deal with variables
    for i, cell in enumerate(table[0]):
        cell.add(chr(65+i))

    # Deal with terminals


if __name__ == '__main__':
    read_grammar()
    r = read_input()
    print(r)
    cyk_alg(None, None, "abbabb")

def create_cell(first, second):
    res = set()
    for f in first:
        for s in second:
            res.add(f+s)
    return res


def read_grammar(filename="./grammar.txt"):
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


def cyk_alg(V, T, inp):
    length = len(inp)

    table = [[set() for _ in range(length-i)] for i in range(length)]

    # Deal with variables
    for i, cell in enumerate(table[0]):
        cell.add(chr(65+i))

    # Deal with terminals
    read_grammar()


if __name__ == '__main__':
    cyk_alg(None, None, "abbabb")

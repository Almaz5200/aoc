# Usefull tools to sometimes use!

adj4 = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
adj8 = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]


def nums(str, separator=None):
    if separator is None:
        for char in str:
            if not char.isdigit():
                separator = char
                break
    return list(map(int, str.split(separator)))


def valPos(r, c, R, C):
    return r in range(R) and c in range(C)

from typing import Set


def distinct_powers(x: int, y: int) -> Set[int]:
    """
    Calculate the set of distinct powers of a**b
    for values of a and b between x and y inclusive.
    """
    pows = set()
    for a in range(x, y+1):
        for b in range(x, y+1):
            pows.add(a**b)

    return pows


print(len(distinct_powers(2, 100)))

def compute(n: int):
    """Compute accumlation sum of inverse number of the sum from 1 to N"""

    out = 0
    for i in range(1, n + 1):
        term = 0
        for j in range(1, i + 1):
            term += j

        out += 1/term

    return out



print(compute(99))

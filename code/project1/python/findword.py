def stats(content : str):
    stats = {}
    for c in content:
        stats[c] = stats.get(c, 0) + 1
    return stats


def findword(content : str):
    contentl = []
    for i in range(len(content)):
        contentl.append(content[i]) # x #

    out = []
    for i in range(65, 123):
        idx = 0
        for j in range(len(content)):
            if contentl[j] == chr(i):
                idx += 1
        out.append((i, idx))


    for t in out:
        print(chr(t[0]), "  ", t[1])



if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(stats("hello"))
    print(findword("hello"))
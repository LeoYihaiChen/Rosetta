def loblozuse(n = 1):
    a = 1
    b = 2
    out = []
    for i in range(n):
        out.append(a)
        out.append(b)      
        a = a + b
        b = a + b
    fout = out[n]
    return fout

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(loblozuse(1))
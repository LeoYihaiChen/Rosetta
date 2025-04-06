def x2n():
    out = []
    a = 1
    for i in range(16):
        out.append(a)
        a = a * 2
        
    return out

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(x2n())
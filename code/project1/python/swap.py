def swap_ai(a = 1, b = 2):
    a, b = b, a
    return a, b

def swap_mine(a = 1, b = 2):
    swapmidnum = a
    a = b
    b = swapmidnum
    return a, b

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(swap_ai(), swap_mine())
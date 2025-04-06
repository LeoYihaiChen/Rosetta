def countdown(n:int = 10)->list:
    out = []
    for i in range(0, n):
        out.append(n-i)
    return out

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(countdown())
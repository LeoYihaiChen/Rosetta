def power(a, b):
    if b <= 0:
        return 0
    if b == 1:
        return a
    
    return power(a, b - 1) * a

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(pow(2, 5))
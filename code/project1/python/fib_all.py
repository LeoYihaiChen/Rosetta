def fibonacci_leo(n = 1):
    a = 0
    b = 1

    out = []

    for i in range(n // 2):
        out.append(a)
        out.append(b)
        a, b = a + b, a + 2*b

    if n % 2:
        out.append(a)

    return out


if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(fibonacci_leo(10))

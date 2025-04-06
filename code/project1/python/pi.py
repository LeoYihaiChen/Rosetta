def calculate_pi(num = 100000):
    pi = 0
    for i in range(num):
        term = (-1) ** i / (2 * i + 1)
        pi += term
    pi *= 4
    return pi

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(calculate_pi())
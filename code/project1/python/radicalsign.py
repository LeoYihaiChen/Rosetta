def radical_sign(n):
    return n ** 0.5

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    n = int(input("Enter a number: "))
    print(f"The radical sign of {n} is {radical_sign(n)}")
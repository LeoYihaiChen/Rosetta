def count(a = 0, b = 100):
    output = []
    for i in range(a, b + 1):
        output.append(i)      
    return output

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(count())

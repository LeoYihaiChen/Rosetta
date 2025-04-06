def rangeplus(n):
    j = []
    for i in range(1, n+1):
        j.append(i)
    return j
    
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(rangeplus(5))
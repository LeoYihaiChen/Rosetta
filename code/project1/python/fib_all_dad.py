def fibonacci_hdc(n = 1):
    if n <= 0:
        return []
    
    if n == 1:
        return [1]
    
    if n == 2:
        return [1, 2]
    
    seq = [1, 2]
    
    for i in range(2, n):
        m = seq[i-2]
        n = seq[i-1]
        seq.append(m+n)
    
    return seq

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(fibonacci_hdc(1))
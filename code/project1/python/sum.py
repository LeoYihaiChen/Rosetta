test_num = 5 

def sum(N = test_num):
    result = 0    
    for i in range(1, N+1):
        result += i
    
    return result


def recursive_sum(N = test_num):
    if N <= 0:
        print("Invalid input", N)
        return 0
    
    if N == 1:
        return 1
    
    return recursive_sum(N-1) + N
    
      
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(sum(test_num), recursive_sum(test_num))
    
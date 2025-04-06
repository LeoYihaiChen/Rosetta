#! RSX : recursive "x"

def recursive_x(n = 5):
    if n <= 0:
        print("invalues input")
        return 0
    
    if n == 1:
        return 1
    
    return recursive_x(n - 1) * n
    

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(recursive_x(5))
from fib_use_dad import fibonacci_recursive
import random
def fibbnocci_recursive_leo(n):
    if n < 0:
        return 0
    if 0 <= n <= 2:
        return n
    return fibbnocci_recursive_leo(n-1) + fibbnocci_recursive_leo(n-2)


def test_fibbnocci_recursive_leo():  #! only for fibbnocci_recursive_leo define.
    n = random.randint(1, 10)
    if fibbnocci_recursive_leo(n) != fibonacci_recursive(n):
        print(f"random number = {n}")
        print(f"Error: fibbnocci_recursive_leo = {fibbnocci_recursive_leo(n), 16}\
, fibonacci_recursive_dad = {fibonacci_recursive(n)}")
        return "Error"
    
        
    else:
        print(f"random number = {n}, output both = {fibbnocci_recursive_leo(n)}")
        print("fibonacci_recursive_test: ")
        return "OK"

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print("test")
    print(fibbnocci_recursive_leo(5))
    print(test_fibbnocci_recursive_leo())
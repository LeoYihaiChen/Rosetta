#! MCF : maximum common factor

def calculate_factors_all(n):
    out = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            out.append(i)

    out.append(n)
            
    return out

def find_shared_max(a_list, b_list):
    a_index = len(a_list) - 1
    b_index = len(b_list) - 1
    
    while a_index >= 0 and b_index >= 0:
        a = a_list[a_index]
        b = b_list[b_index]
        
        if a == b:
            return a
        
        if a > b:
            a_index -= 1
        else:
            b_index -= 1
    

def Maximum_common_factor(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return 0
    
    if a <= 0 or b <= 0:
        return 0
    
    if a % b == 0:
        return b
    
    if b % a == 0:
        return a
    
    a_factors = calculate_factors_all(a)
    b_factors = calculate_factors_all(b)
    return find_shared_max(a_factors, b_factors)

def testofMaximum_common_factor():
    testnum = (40, 60)
    output = Maximum_common_factor(40, 60)
    print(f"input to the define will be {testnum}")
    print(f"output = {output}")
    if output == 0 or output != 20:
        if output == 0:
            print("Error: no common factor found between the two lists")
        if output != 20:
            print("Error: output is not true")
        return "Error"
    else:
        print("output is true")
        return "OK"


if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(testofMaximum_common_factor())
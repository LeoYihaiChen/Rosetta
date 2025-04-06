def primenum_use(inp = 20):
    if inp <= 0:
        print("invalid input")
        return 0
    
    elif inp == 1:
        return False 
    
    if inp % 2 == 0:
        return False
    
    for i in range(2, int(inp / 2) + 1):
        if inp % i == 0:
            return False
    
    return True



def primenum_all_2x():
    out = []
    for i in range(1, 100, 2):
        if primenum_use(i) == False:
            pass
        else:
            out.append(i)
    return out


if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(primenum_all_2x())
    print(primenum_use(18))
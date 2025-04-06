def mate10(lista : list) -> bool:
    noc = 0
    for i in lista:
        match i:
            case 10:
                return True
            case _:
                noc += 1
                
    if noc == len(lista):
        return None
                

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(mate10([1, 2, 3, 4, 10]))
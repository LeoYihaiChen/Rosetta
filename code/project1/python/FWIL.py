#! FWIL : find word in list

def findwordinlist(inputlist:list, findword:str) -> bool:
    print("findwordinlist define start:")
    print("   | create by Leo 2024/05/01")
    print("   | ")
    print("   | ")

    ## Error detection：
    print("   | Error detection ...")
    # type Error:
    type_inputlist = type(inputlist)
    if type_inputlist != list:
        print("   | Type Error:")
        print(f"   | Input type of inputlist: {type_inputlist}")
        print("   | Correct type:<class 'list'>")
        print("   | Error detection: Error")
        print("   | ")
        print("   | ")
        print("findwordinlist define end")
        return
    type_findword = type(findword)
    if type_findword != str:
        print("   | Type Error:")
        print(f"   | Input type of findword: {type_findword}")
        print("   | Correct type: <class 'str'>")
        print("   | Error detection: Error")
        print("   | ")
        print("   | ")
        print("findwordinlist define end")
        return
    print("   | Error detection OK")  
    print("   | ")  

    ## initialization:
    print("   | initialization ...")
    long = len(inputlist)
    have = False
    print("   | initialization OK")
    ## calculate:
    print("   | ")
    print("   | caculate ...")
    for i in range(0, long - 1):
        rangethings = inputlist[i]
        if rangethings == findword:
            have = True
        else:
            have = False
    print("   | caculate OK")
    print("   | ")
    print("   | return:")
    print(f"   | {have}")
    print("   | ")
    print("   | ")
    
    print("findwordinlist define end")
    return have
    

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(findwordinlist(["A", "c", ",", "3", "Ac,3", " "], "AC.3"))
    
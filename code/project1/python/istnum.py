def biggistnum(inplist:list)->tuple:
    print("biggistnum define start:")
    print("   | create by Leo 2024/05/02")
    print("   | ")
    print("   | ")
    ## Error detection
    print("   | Error detection ...")
    if not isinstance(inplist, list):
        print("   | Type Error:")
        print(f"   | Input type of inputlist: {type(inplist)}")
        print("   | Correct type:<class 'list'>")
        print("   | Error detection:Error")
        print("   | ")
        print("   | ")
        print("findwordinlist define end")
        return
    else:
        print("   | Error detection: OK")
        
    ## initialization:
    print("   | ")
    print("   | initialization ...")
    long = len(inplist)
    biggistind = 0
    biggistnumber = inplist[biggistind]
    print("   | initialization: OK")
    
    ## calculate:
    print("   | ")
    print("   | caculate ...")
    for i in range(1, long):
        i_num = inplist[i]
        if i_num >= biggistnumber:
            biggistind = i  # biggistnum refresh
            biggistnumber = i_num
    print("   | caculate OK")
    print("   | ")
    print("   | return(tuple):")
    print(f"   | [0] num = {biggistnumber}")
    print(f"   | [1] index = {biggistind}")
    print("   | ") 
    print("   | ")
    print("biggistnum define end")
    return (biggistnumber, biggistind)


def smallistnum(inplist:list)->tuple:
    print("smallistnum define start:")
    print("   | create by Leo 2024/05/02")
    print("   | ")
    print("   | ")
    ## Error detection
    print("   | Error detection ...")
    if not isinstance(inplist, list):
        print("   | Type Error:")
        print(f"   | Input type of inputlist: {type(inplist)}")
        print("   | Correct type:<class 'list'>")
        print("   | Error detection:Error")
        print("   | ")
        print("   | ")
        print("findwordinlist define end")
        return
    else:
        print("   | Error detection: OK")
        
    ## initialization:
    print("   | ")
    print("   | initialization ...")
    long = len(inplist)
    smallistind = 0
    smallistnumber = inplist[smallistind]
    print("   | initialization OK")
    
    ## calculate:
    print("   | ")
    print("   | caculate ...")
    for i in range(1, long):
        i_num = inplist[i]
        if i_num <= smallistnumber:
            smallistind = i  # smallistnum refresh
            smallistnumber = i_num
    print("   | caculate OK")
    print("   | ")
    print("   | return(tuple):")
    print(f"   | [0] num = {smallistnumber}")
    print(f"   | [1] index = {smallistind}")
    print("   | ") 
    print("   | ")
    print("smallistnum define end")
    return (smallistnumber, smallistind)

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(biggistnum([1, 5, 3, 2, 4]))
    print(smallistnum([1, 5, 3, 2, 4]))
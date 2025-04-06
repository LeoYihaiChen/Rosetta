def feboloz(num:int, mode:int):
    #! num:int, mode:int, output:any
    #! mode:1 --> all
    #! mode:2 --> use
    if type(num) != int:
        #! invalid input
        print("Error:")
        print("invalid type inputnum")
        print("correct type of num is int type")
        print(f"type of the input num = {type(num)} type")
        return 0
    
    elif type(mode) != int:
        #! invalid input
        print("Error:")
        print("invalid type inputnum")
        print("correct type of mode is int type")
        print(f"type of the input mode = {type(mode)} type")
        return 0
    
    elif mode != 1 and mode != 2:
        #! invalid input
        print("Error:")
        print("invalid input")
        print(f"input of mode = {mode}")
        print("correct input of mode = 1 or 2")
        print("1: all mode | 2: use mode")
        return 0
    
    if mode == 1:
        #! all mode
        out = [0, 1]
        if num == 0:
            #! invalid input
            return 0
        for f in range(2, num+1):
            out.append(out[f-2]+out[f-1])
        return out
            
    elif mode == 2:
        #! use mode
        if num == 0:     
            #! invalid input
            return 0
        if num == 1:
            return num
        return feboloz(num - 1, 2) + feboloz(num - 2, 2)

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print((feboloz(5, 1), feboloz(5, 2)))
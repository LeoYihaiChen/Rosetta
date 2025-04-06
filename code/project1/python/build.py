def build(string : str, system : int) -> int:
    if type(string) != str:
        print("Error:")
        print("invaild type of string")
        return 0
    elif type(system) != int:
        print("Error:")
        print("invaild type of system")
        return 0
    if system != 2 and system != 8 and system != 16:
        print("sorry, this define unsupported this number system.")
        print("supported number system:")
        print("10 --> 2, 8, 16")
        return
    out = []
    for i in range(len(string)):
        inter = int(ord(string[i]))
        if system == 2:
            out.append(bin(inter))
        elif system == 8:
            out.append(oct(inter))
        elif system == 16:
            out.append(hex(inter))
    return out

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(build("python", 16))
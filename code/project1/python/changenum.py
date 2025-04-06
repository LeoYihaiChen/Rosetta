def allchangenum():
    out = []
    
    for i in range(1, 256):
        if i != 1:
            out.append("  ||  ")
        out.append(i)
        out.append(bin(i))
        out.append(hex(i))
        out.append(chr(i))
    return out
        
print(allchangenum())
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(allchangenum())
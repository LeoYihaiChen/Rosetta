def pow1000all():
    import math
    il = []
    ol = []
    for i in range(1,100):
        il.append(i)
        o = int(math.pow(i, i))
        ol.append(o)
        if o >= 1000:
            del il[-1]
            del ol[-1]
            break
    
    for i in range(len(ol)):
        print(il[i], ol[i])
    return ""

def pow1000use(num:int):
    import math
    out = math.pow(num, num)
    if out >= 1000:
        print(f"output is bigger than 1000")
        return ""
    else:
        return out
    
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(pow1000all())
    print(pow1000use(25))
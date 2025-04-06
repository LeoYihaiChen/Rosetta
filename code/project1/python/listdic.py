from dc import familydic
def familymembersdic(who:int, characteristic:str)->any:
    global familydic
    if who == 1:
        out = familydic.yizhou[characteristic]
    elif who == 2:
        out = familydic.yihai[characteristic]
    elif who == 3:
        out = familydic.huidong[characteristic]
    elif who == 4:
        out = familydic.weiqing[characteristic]
    
    return out

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(familymembersdic(2, "love "))
def exersize():
    while True:
        t = 0
        f = 0
        tf = True
        for i in range(30):
            if tf:
                term = chr(do())
            print(f"Please press {term}")
            a = input(">>> ")
            if correct(term, a) == False:
                print("wrong anser -------------------------- wrong")
                f += 1
            else:
                print("right anser")
                t += 1
        print("right:" + str(t) +"  "+
              "wrong:" + str(f))
        if yn():
            break
        else:
            wait()




def yn():
    more = input(" More exersizes? \n Y -> Yes | N -> No \n>>> ")
    if more == "Y" or more == "y":
        break_ = False
        print("Please have a break.")
    elif more == "N" or more == "n":
        break_ = True
    else:
        print("wrong index")
        yn()

    return break_
def correct(q, a):
    if q != a:
        return False
    else:
        return True

def wait():
    import time
    for i in range(20, 0, -1):
        print(f"lasttime:{i}")
        print(f"|{sum(i, ">")}{sum(20-i, " ")}|")
        time.sleep(1)


def do():
    import random
    _do = random.randint(97, 122)
    return _do

def sum(num, word):
    out = ""
    for i in range(0, num):
        out += word
    return out

exersize()
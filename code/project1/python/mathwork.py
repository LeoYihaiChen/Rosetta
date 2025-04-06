def mathwork(mode : int):
    import random as rad
    import time as t
    wrong = 0
    true = 0
    wa = 0
    wt = 0
    i = input("Press S to Start, press Q to quit: \n")
    if i == "S" or "s":
        pass
    elif i == "Q" or "q":
        return
    if mode == 1:
        for i in range(4):
            time = 0
            while time <= 21:
                time += 1
                if time >= 21:
                    break
                a = rad.randint(1, 20)
                b = rad.randint(1, 20)
                ans = input(f"{a} x {b} = ")
                if ans != str(a * b):
                    print("anser is wrong!")
                    wrong += 1
                else:
                    print("anser is true!")
                    true += 1
            if i != 3:
                htg = input("Press S to Start, press Q to quit: \n")
                if i == "S" or "s":
                    pass
                elif i == "Q" or "q":
                    return
                print("have a break: 10 sec")
                t.sleep(10)
            print(f"True:{true}, False:{wrong}")
            wa += wrong
            wt += true
        print(f"True:{wt}, False:{wt}")
    elif mode == 2:
        for i in range(4):
            time = 0
            while time <= 21:
                time += 1
                if time >= 21:
                    break
                a = rad.randint(1, 10)
                b = rad.randint(1, 10)
                ans = input(f"{a} + {b} = ")
                if ans != str(a + b):
                    print("anser is wrong!")
                    wrong += 1
                else:
                    print("anser is true!")
                    true += 1
            if i != 3:
                htg = input("Press S to Start, press Q to quit: \n")
                if i == "S" or "s":
                    pass
                elif i == "Q" or "q":
                    return
                print("have a break: 10 sec")
                t.sleep(10)
            print(f"True:{true}, False:{wrong}")
            wa += wrong
            wt += true
        print(f"True:{wt}, False:{wt}")
    elif mode == 3:
        for i in range(4):
            time = 0
            while time <= 21:
                time += 1
                if time >= 21:
                    break
                a = rad.randint(10, 20)
                b = rad.randint(1, 10)
                ans = input(f"{a} - {b} = ")
                if ans != str(a - b):
                    print("anser is wrong!")
                    wrong += 1
                else:
                    print("anser is true!")
                    true += 1
            if i != 3:
                htg = input("Press S to Start, press Q to quit: \n")
                if i == "S" or "s":
                    pass
                elif i == "Q" or "q":
                    return
                print("have a break: 10 sec")
                t.sleep(10)
            print(f"True:{true}, False:{wrong}")
            wa += wrong
            wt += true
        print(f"True:{wt}, False:{wt}")


if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(mathwork(1))
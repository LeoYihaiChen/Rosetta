def Cracking_Passwords_6x(correctpassword) -> int:
    trypassword = 0
    for i in range(0, 999999): 
        print(trypassword)
        trypassword += 1
        if trypassword == correctpassword:
            print(f"{trypassword} True")
            print(f"correctpassword is {trypassword}")
            return trypassword


def Cracking_Passwords_6x_test():
    import random
    testnum = random.randint(0, 999999)
    print(testnum)
    if Cracking_Passwords_6x(testnum) == testnum:
        print("OK")
        return "OK"
    else:
        print("Error")
        return "Error"
        
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(Cracking_Passwords_6x_test())
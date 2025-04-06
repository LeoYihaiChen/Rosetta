import time
def startcounter():
    for i in range(3, 0):
        print(i)
        time.sleep(1.0)
        if i <= 0:
            break
        
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(startcounter())
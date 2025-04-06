#! TCD:time count down

def timecountdown(timei : int) -> None:
    import time
    for i in range(0, timei+1):
        if timei-i == 0:
            print("time it!")
            break
        print(timei-i)
        time.sleep(1)


if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(timecountdown(3))
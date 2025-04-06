from fib_all import fibonacci_leo

finall_num = None
borurline = fibonacci_leo(50)
num_use = 50
def golden_ratio():
    global finall_num, borurline, num_use
    for i in range(1, num_use):
        term = borurline[i-1] / borurline[i]
        print(term)
    return 'finish'


def golden_split_point_HDC(N: int = 100):
    array = [0, 1]
    for i in range(N):
        array[i%2] = array[0] + array[1]
        ratio = array[(i+1)%2]/array[i%2]
        print(f"ratio[{i}] = {ratio:.64f}")

if __name__ == '__main__':
    print(f"Executing {__file__}: {__name__}")
    #print(golden_ratio())
    golden_split_point_HDC(1000)

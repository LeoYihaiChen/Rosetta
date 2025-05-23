import random

def randomn(sum, num):
    list = []
    for i in range(num  ):
        list.append(random.randint(1, sum))
    out = []
    for i in range(sum):
        out.append(0)
    for i in range(1, sum):
        out[list[i-1]] += 1
    return out

if __name__ == "__main__":
    print("Excuting: random.py")
    print(randomn(3, 10))
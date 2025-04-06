import random
from FWIL import findwordinlist

def forlist(list):
    out = []
    for i in list:
        out.append(i)
    return out

def test_forlist(testlists): # 仅限于forlist函数
    for testlist in testlists:
        print(f"testlist = {testlist}")

        result = forlist(testlist)
        print("output = ", result)

        if result != testlist:
            print("output error")

def testlists():
    out = []
    for i in range(10):
        lists = []
        for j in range(random.randint(1, 19)):
            i = random.randint(1, 20)
            if findwordinlist(lists, str(i)):
                continue
            lists.append(i)
        out.append(lists)
    return lists





if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")

    testdata = testlists()
    print(testdata)
    print(test_forlist(testdata))
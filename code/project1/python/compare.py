def compare_smallist_num(line):
    idx = 0
    for i in range(0, len(line)):
        if line[i] < line[idx]:
            idx = i
            
    return line[idx]


def compare_biggist_num(line):
    idx = 0
    for i in range(0, len(line)):
        if line[i] > line[idx]:
            idx = i
            
    return line[idx]


def test_smallist_num(): # only for smallistnum define
    import random
    out = []
    for i in range(100):
        j = random.randint(0, 100)
        out.append(j)
        
    return out, compare_smallist_num(out)


def test_biggist_num(): # only for biggistnum define
    import random
    out = []
    for i in range(100):
        j = random.randint(0, 100)
        out.append(j)
        
    return out, compare_biggist_num(out)

 
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(test_smallist_num())
    print()
    print(test_biggist_num())
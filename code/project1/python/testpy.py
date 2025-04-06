# 1 # python ==========================================|| 1 
string = "123"
integer = int(string)
print(integer)
# output # 123
print()
# 2 # python ==========================================|| 2 
num = 65
letter = chr(num)
print(letter)
# output # A
print()
# 3 # python ==========================================|| 3 
for i in range(10):
    if i == 5:
        continue
    print(i)
# output # 012346789
print()
# 4 # python ==========================================|| 4 
for i in range(10):
    if i == 5:
        break
    print(i)
# output # 01234
print()
# 5 # python ==========================================|| 5 
list_big = []
for i in range(2):
    list_small = []
    for j in range(3):
        list_small.append(i*3+j)
    list_big.append(list_small)
print(list_big)
# output # [[0, 1, 2], [3, 4, 5]]
print()
# 6 # python ==========================================|| 6 
grid_big = []
for i in range(2):
    grid_middle = []
    for j in range(3):
        grid_small = []
        for k in range(4):
            grid_small.append((i*12+j*4)+k)
        grid_middle.append(grid_small)
    grid_big.append(grid_middle)
print(grid_big)
# output # [[[0, 1, 2, 3], [3, 4, 5, 6], ...
print()
# 7 # python ==========================================|| 7 
def defineabob(a):
    if a <= 0:
        return 0
    if a == 1:
        return 1

    returnc = defineabob(a - 2) + defineabob(a - 1)
    return returnc

print(defineabob(10))

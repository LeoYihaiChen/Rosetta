def caculate(num):
    if type(num) != int:
        return TypeError
    if num <= 0:
        return SyntaxError
    elif num == 1:
        return 1
    else:
        return num * caculate(num-1)


print(caculate(200))
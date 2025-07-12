import random
num = random.randint(2,9)
if num <= 5:
    print(1, "X",num, "=", 1*num)
    print(2, "X",num, "=", 2*num)
    print(3, "X",num, "=", 3*num)
    print(4, "X",num, "=", 4*num)
    print(5, "X",num, "=", 5*num)
else:
    print(5, "X",num, "=", 5*num)
    print(4, "X",num, "=", 4*num)
    print(3, "X",num, "=", 3*num)
    print(2, "X",num, "=", 2*num)
    print(1, "X",num, "=", 1*num)
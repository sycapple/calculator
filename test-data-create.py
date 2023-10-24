import random


# 生成一个随机整数或浮点数


def random_number():
    n = random.randint(0, 1)
    if (n == 1):
        num = random.randint(0, 10000)
        return str(num)
    else:
        num = random.uniform(0, 10000)
        return format(num, '.1f')


# 符号序列
x = ["+", "-", "*", "/", "^"]
f = open("test.txt", 'w')

# 随机生成250个算式读入txt
for i in range(251):
    formula = ''
    m = random.randint(2, 4)
    for q in range(m):
        num = random_number()
        if (formula != ''):
            if (formula[-1] == '/'):
                while (num == '0'):
                    num = random_number()
        if (num[0] == '-'):
            s = '(' + num + ')'
            formula += s
        else:
            formula += num
        if (q != (m - 1)):
            formula += random.choice(x)
    f.write(formula + '\n')
    i += 1

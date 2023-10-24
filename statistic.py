def statistic(ls):
    lls = []
    lx = ['num', 'N_cf', 'N_cs', 'N_uf', 'N_us', 'N_c', 'N_u', 'N_f', 'N_s']
    lls.append(lx)
    N_cf = {}
    N_cs = {}
    N_uf = {}
    N_us = {}
    for i in range(31):
        N_cf[i] = 0
        N_cs[i] = 0
        N_uf[i] = 0
        N_us[i] = 0
    for i in range(len(ls)):
        if (i != 0):
            if (ls[i][-1][:-1] == ls[i][-2]):
                flag = 1
            else:
                flag = 0
            for q in range(31):
                if (ls[i][q + 1] == '0'):
                    if (flag == 1):
                        N_us[q] += 1
                    else:
                        N_uf[q] += 1
                else:
                    if (flag == 1):
                        N_cs[q] += 1
                    else:
                        N_cf[q] += 1
    for i in range(31):
        lss = [i, N_cf[i], N_cs[i], N_uf[i], N_us[i],
               N_cf[i] + N_cs[i], N_uf[i] + N_us[i], N_cf[i] + N_uf[i], N_cs[i] + N_us[i]]
        # lls = [桩点序号，cf执行桩点但失败个数，cs执行且成功，uf未执行且失败，us执行且成功,c执行，u未执行,f案例失败，s成功]
        lls.append(lss)
    return lls


def main():
    f = open("output.csv")
    ls = []
    for line in f:
        line = line.replace("\n", " ")
        ls.append(line.split(","))
    lls = statistic(ls)
    f_statitic = open(
        "statistic.csv", 'w')
    for items in lls:
        print(items)
        f_statitic.write(','.join('%s' % id for id in items) + '\n')
    f_statitic.close()
    f.close()

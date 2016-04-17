import math as ma

def cosSim(x, y):
    i = len(x) - 1
    sumX = 0
    sumY = 0
    sumXY = 0
    while(i >= 0):
        sumX = sumX + x[i]**2
        sumY = sumY + y[i]**2
        sumXY = sumXY + x[i]*y[i]
        i -= 1
    return sumXY/(ma.sqrt(sumX) * ma.sqrt(sumY));


#皮尔逊相似度: cov(X, Y)/sqrt(X的方差*Y的方差） == (E(XY) - E(X)E(Y)]/ [(sqrt(E(X2) - E2(X))) * sqrt(sqrt(E(Y2) - E2(Y))))
def pearsSim(x, y):
    n = len(x)
    EX = 0
    EY = 0
    EX2 = 0
    EY2 = 0
    EXY = 0
    i = 0
    while(i < n):
        EX = EX + x[i];
        EX2 = EX2 + x[i]**2
        EY = EY + y[i]
        EY2 = EY2 + y[i]**2
        EXY = EXY + x[i]*y[i]
        i = i + 1
    EX = EX/n
    EY = EY/n
    EXY = EXY/n
    EX2 = EX2/n
    EY2 = EY2/n
    if((ma.sqrt(EX2 - EX**2) * ma.sqrt(EY2 - EY**2)) == 0):
        return 0
    return (EXY - (EX * EY)) / (ma.sqrt(EX2 - EX**2) * ma.sqrt(EY2 - EY**2))


def ecludSim(x, y):
    i = len(x) - 1
    sumXY = 0
    while(i >= 0):
        sumXY = sumXY + (x[i] - y[i]) * (x[i] - y[i])
        i -= 1
    return ma.sqrt(sumXY)
        

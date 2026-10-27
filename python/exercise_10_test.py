import math
#p an odd prmenumber

def F_p(p: int) -> [int]:
    Fp = []
    for i in range(0, p):
        Fp.append(i)
    return Fp

def addinFp(a,b,p):
    return (a+b) % p

#a^p
def powerinFp(a: int, q: int, p: int)->int:
    return math.pow(a,q) % p


def F_psqr(Fp: [int])-> [(int, int)]:
    Fp2 = []
    for i in Fp:
        for j in Fp:
            Fp2.append((i,j))
    return Fp2

#b \in Fp
def setE(Fp2: [(int, int)],b: int, p: int):
    E = []
    for (x,y) in Fp2:
        if(powerinFp(y,2,p) == addinFp(powerinFp(x,3,p),b,p)):
            E.append((x,y))
    return E

def setpwcubx(Fp,p):
    X = []
    for i in Fp:
        X.append(powerinFp(i, 3, p))
    return X

def setpwsqx(Fp,p):
    X = []
    for i in Fp:
        X.append(powerinFp(i, 2, p))
    return X

if __name__ == '__main__':
    p = 7
    Fp = F_p(p)
    #X = setpwcubx(Fp, p)
    #print(X)
    Y = setpwsqx(Fp, p)
    print(Y)
    Fp2 = F_psqr(Fp)
    E = setE(Fp2, 5, p)
    #print(E)
    #print(len(E))

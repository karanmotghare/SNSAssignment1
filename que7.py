import sys


def get_euc_coeff(a, b):

    if(b == 0):

        return a, 1, 0

    g, x0, y0 = get_euc_coeff(b, a % b)

    y = x0-(a//b)*y0

    x = y0

    return g, x, y

def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)

def congurence(a,b,m,g):

    print("Y",end=" ")

    print(g,end=" ")

    bb = b//g

    aa = a//g

    mm = m//g

    gg,x,y = get_euc_coeff(aa,mm)

    f1 = (bb*x) % mm

    dif=0

    ans = []

    while(len(ans)!=g):

        ans.append(f1+dif)

        dif += mm

    for x in ans:

        print(x,end=" ")


ip = sys.argv[1:]

a = int(ip[0])

b = int(ip[1])

m = int(ip[2])

g = gcd(a,m)

if(b%g==0):
    congurence(a,b,m,g)
else:
    print("N",end=" ")


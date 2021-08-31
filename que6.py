import sys


def gcd(a, b):

    if b == 0:
        return a

    return gcd(b , a%b)


def get_euc_coeff(a, b):

    if(b == 0):

        return a, 1, 0

    g, x0, y0 = get_euc_coeff(b, a % b)

    y = x0-(a//b)*y0

    x = y0

    return g, x, y

def inverse(a,m):

    if(gcd(a,m)==1):

        print("Y",end=" ")

        g,x,y=get_euc_coeff(a,m)

        x=(x+m)%m

        print(x,end=" ")
    
    else:

        print("N",end=" ")

def main():
    
    a = int(sys.argv[1])
    
    m = int(sys.argv[2])
    
    inverse(a,m)

if __name__ == '__main__':
    main()

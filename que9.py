import sys


def getDivisors(n):
    i = 1
    divisors = []
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            if n/i != i:
                divisors.append(n//i)
        i += 1
    return divisors

def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)

def phi_val(m):

    count = 0
    
    for i in range(1, m):

        g = gcd(m, i)

        if g == 1:
            count += 1

    return count

ip = sys.argv[1:]

a = int(ip[0])

m = int(ip[1])

if(gcd(a,m)==1):
    
    q = phi_val(m)
    
    div = sorted(getDivisors(q))

    flag=0

    for d in div:

        if((a**d)%m==1):

            print(d,end=" ")
            flag=1
            break

    if(flag==0):
        print(q,end=" ")       
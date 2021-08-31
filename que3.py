import sys
from math import sqrt

def is_prime(n):
    
    if(n>1):
        
        for x in range(2,int(sqrt(n))+1):

            if( n%x == 0 ):
    
                return False

        return True
    
    else:
        return False

def get_primes(n):
    
    ans=[]

    for i in range(1,n+1):

        if(is_prime(i)):

            ans.append(i)
    
    return ans


def main():

    ip = sys.argv[1:]

    n = int(ip[0])

    prm = get_primes(n)

    fac = []

    i = 0

    while(n != 1):

        x = prm[i]

        while(n%x == 0):

            n = n//x

            fac.append(x)

        i+=1

    for k in fac:
        
        print(k,end=" ") 



if __name__ == '__main__':

    main()

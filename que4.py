import sys

def gcd(a,b):
    
    if(b==0):
        
        return a
    
    return gcd(b,a%b)

def get_rrsm(m):

    ans = [] 

    for x in range(1,m):

        g = gcd(m,x)

        if (g==1):

            ans.append(x)
    
    return ans


def main():

    ip = sys.argv[1:]

    m = int(ip[0])

    rrsm = get_rrsm(m)

    for i in rrsm:

        print(i,end=" ")
    
    print("phi(m) =",len(rrsm),end=" ")


if __name__ == '__main__':

    main()

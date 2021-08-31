import sys

def gcd(a,b):
    
    if(b==0):
        return a
    
    return gcd(b,a%b)

def getgcd(ip):

    gd = int(ip[0])
    
    for x in range(1,len(ip)):
        
        gd=gcd(gd,int(ip[x]))
    
    return gd

def getcommondiv(gcd):
    
    opt=[]
    
    for x in range(1,gcd+1):

        if(gcd%x==0):

            opt.append(x)

    return opt

def main():

    ip=sys.argv[2:]
    
    gcd=getgcd(ip)
    
    opt=getcommondiv(gcd)
    
    for i in opt:
        
        print(i,end=" ")

if __name__ == '__main__':
    
    main()


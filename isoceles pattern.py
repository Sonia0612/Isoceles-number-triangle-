
#using while function
def while_func(n):
    i=1
    while i<=n:
        #spaces
        j=1
        while j<=n-i:
            print(" ",end="")
            j=j+1
        
        k=i
        while k<=2*i-1:
            print(k,end="")
            k=k+1
        k=k-2
        while k>=i:
            print(k,end="")
            k=k-1
        i=i+1
        print()
n=int(input())
while_func(n)

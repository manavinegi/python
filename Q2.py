def fact():
    n=int(input("factorial of number: "))
    fa=1
    for i in range(1,n+1):
        fa*=i
    print("factorial is",fa)    
        
def prime():
    n=int(input("range of prime nos :"))
    print('2')
    for i in range(3,n+1):
        f=0
        for j in range(2,i):
            
            if i%j==0:
                f=1
                continue
        if f==0:
            print(i)

def fab():
    n=int(input("number of terms: "))
    if n==1:
        print('0')
    elif n==2:
        print("0")
        print("1")

    elif n>2:
        f=0
        s=1
        print(f)
        print(s)
        i=0
        while i<=n-2:
            t=s+f
            print(t)
            f=s
            s=t
            i=i+1

print("1.FACTORIAL\n2.PRIME NUMBERS\n3.FIBONACCI SERIES")

cho=int(input("choice: "))

if cho==1:
    fact()
elif cho==2:
    prime()
elif cho==3:
    fab()
else:
    print("invalid entry")
      

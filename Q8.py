a=input("Enter a string: ")
def lenght_str():
    f=len(a)
    print("The lenght of the entered string is",f)

def conc_str():
    b=input("Enter string to concatenate: ")
    print("The concatenation of sting is",a+b)

def rev_str():
    c=a[::-1]
    print("The reverse of the entered str is",c)

def compare():
    s1=input("string 1: ")
    s2=input("string 2: ")
    n1=len(s1)
    n2=len(s2)
    if n1>n2:
        print("String 1 is longer than String 2")
    elif n1==n2:
        print("String 1 is of the same length as String 2")
    else:
        print("String 1 is shorter than String 2")
        
def search():
    st=input("enter string: ")
    sub=input("enter substring to be searched: ")
    f=0

    for i in range(len(st)):
        for j in range(len(st)):
            if st[i:j]==sub:
                print("substring found at:",i)
                f=1
                break
    if f==0:
        print("substring not found")
            
    
print("1.LENGTH OF STRING\n2.CONCATENATE TWO STRINGS\n3.REVERSE STRING\n4.COMPARE STRINGS\n5.SEARCH POSITION OF SUBSTRING")
print()
ch=int(input("Enter choice: "))

if ch==1:
    len_str()    
elif ch==2:
    conc_str()
elif ch==3:
    rev_str()
elif ch==4:
    compare()
elif ch==5:
    search()
